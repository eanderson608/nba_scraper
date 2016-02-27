from urllib.request import urlopen
from bs4 import BeautifulSoup
from NBAScrapeFormat import convert_team_names, get_dates_in_range
import re
import pprint
import time
import json
import os,sys

def main():

	start_date = sys.argv[1]
	end_date = sys.argv[2]
	output_filename = sys.argv[3]

	# get game dates
	game_date_list = get_dates_in_range(start_date, end_date)

	for date in game_date_list:
		get_stats(date, output_filename)

def get_stats(game_date, output_filename):

	# load stat page
	stat_html = urlopen("http://www.donbest.com/nba/odds/" + game_date + ".html")
	stat_bs_obj = BeautifulSoup(stat_html.read(), "html.parser")

	# find stat table in page
	stat_table = stat_bs_obj.find("table")

	# scrape info
	teams = stat_table.findAll("span", {"class":"oddsTeamWLink"})
	final_scores = stat_table.findAll("div", {"id":re.compile("_Div_Score_.*")})
	lines = stat_table.findAll("div", {"id":re.compile("_Div_Line_.*_23$")})

	# remove tags
	teams = [team.text for team in teams]
	final_scores = [float(final.text) for final in final_scores]
	lines = [float(line.text) for line in lines]

	# convert team names (imported from NBAScrapeFormat.py)
	convert_team_names(teams)

	# assemble game dicts
	games = []
	for i in range(len(teams)):

		# for only every pair of teams
		if i % 2 == 0:
			temp_dict = {}
			temp_dict["AwayTeam"] = teams[i]
			temp_dict["AwayFinalScore"] = final_scores[i]
			temp_dict["HomeTeam"] = teams[i + 1]
			temp_dict["HomeFinalScore"] = final_scores[i + 1]
			temp_dict["GameDate"] = game_date

			# calculte stats
			if lines[i] >= 0:
				temp_dict["O/UMargin"] = (final_scores[i] + final_scores[i + 1]) - lines[i]
				temp_dict["HomePSCoverBy"] = (final_scores[i + 1] - final_scores[i]) + lines[i + 1]
				temp_dict["O/U"] = lines[i]
				temp_dict["HomePointSpread"] = lines[i + 1]
			else:
				temp_dict["O/UMargin"] = (final_scores[i] + final_scores[i + 1]) - lines[i + 1]
				temp_dict["HomePSCoverBy"] = (final_scores[i + 1] - final_scores[i]) - lines[i]
				temp_dict["O/U"] = lines[i + 1]
				temp_dict["HomePointSpread"] = -(lines[i])

			# load ref pages and get ref info
			ref_html = urlopen("http://www.basketball-reference.com/boxscores/" + game_date + "0" + temp_dict["HomeTeam"] + ".html")
			ref_bs_obj = BeautifulSoup(ref_html.read(), "html.parser")
			ref_table = ref_bs_obj.find("table", {"class":"margin_top small_text"})

			# find officials and place in dict
			refs = ref_table.find(text="Officials:").parent.next_sibling.text.split(",")
			refs = [ref.upper().strip() for ref in refs]
			temp_dict["Referees"] = refs

			# pretty print
			pp = pprint.PrettyPrinter(indent=0)
			pp.pprint(temp_dict)
			print()

			# give server a break
			time.sleep(1)

			# append dict to json
			f = open(output_filename, 'a')
			json.dump(temp_dict, f)
			f.write(os.linesep)

if __name__ == "__main__":
	main()



		
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# load pages
stat_html = urlopen("http://www.donbest.com/nba/odds/20160222.html")
ref_html = urlopen("http://www.basketball-reference.com/boxscores/201602250BOS.html")
stat_bs_obj = BeautifulSoup(stat_html.read(), "html.parser")
ref_bs_obj = BeautifulSoup(ref_html.read(), "html.parser")

# find tables
stat_table = stat_bs_obj.find("table")
ref_table = ref_bs_obj.find("table", {"class":"margin_top small_text"})

# find officials from basketball-reference, 
# still need to incorproate into dict for loop below
refs = ref_table.find(text="Officials:").parent.next_sibling.text.split(",")
print(refs)


# scrape info
teams = stat_table.findAll("span", {"class":"oddsTeamWLink"})
final_scores = stat_table.findAll("div", {"id":re.compile("_Div_Score_.*")})
lines = stat_table.findAll("div", {"id":re.compile("_Div_Line_.*_23$")})

# remove tags
teams = [team.text for team in teams]
final_scores = [float(final.text) for final in final_scores]
lines = [float(line.text) for line in lines]

# convert team names
for i in range(len(teams)):

	if teams[i] == "New York Knicks":
		teams[i] = "NYK"

	elif teams[i] == "Sacramento Kings":
		teams[i] = "SAC"

	elif teams[i] == "Indiana Pacers":
		teams[i] = "IND"

	elif teams[i] == "Cleveland Cavaliers":
		teams[i] = "CLE"

	elif teams[i] == "Golden State Warriors":
		teams[i] = "GS"

	elif teams[i] == "Orlando Magic":
		teams[i] = "ORL"

	elif teams[i] == "Milwaukee Bucks":
		teams[i] = "MIL"

	elif teams[i] == "Oklahoma City Thunder":
		teams[i] = "OKC"

	elif teams[i] == "Boston Celtics":
		teams[i] = "BOS"

	elif teams[i] == "New Orleans Pelicans":
		teams[i] = "NOP"

	elif teams[i] == "Brooklyn Nets":
		teams[i] = "BRK"

	elif teams[i] == "Phoenix Suns":
		teams[i] = "PHO"

	elif teams[i] == "Houston Rockets":
		teams[i] = "HOU"

	elif teams[i] == "Portland Trail Blazers":
		teams[i] = "POR"

	elif teams[i] == "San Antonio Spurs":
		teams[i] = "SAS"

	elif teams[i] == "Utah Jazz":
		teams[i] = "UTA"

	elif teams[i] == "Philadelphia 76ers":
		teams[i] = "PHI"

	elif teams[i] == "Washington Wizards":
		teams[i] = "WAS"

	elif teams[i] == "Denver Nuggets":
		teams[i] = "DEN"

	elif teams[i] == "Detroit Pistons":
		teams[i] = "DET"

	elif teams[i] == "Miami Heat":
		teams[i] = "MIA"

	elif teams[i] == "Toronto Raptors":
		teams[i] = "ORL"

	elif teams[i] == "Minnesota Timberwolves":
		teams[i] = "MIN"

	elif teams[i] == "Los Angeles Lakers":
		teams[i] = "LAL"

	elif teams[i] == "Atlanta Hawks":
		teams[i] = "ATL"

	elif teams[i] == "Los Angeles Clippers":
		teams[i] = "LAC"

	elif teams[i] == "Memphis Grizzlies":
		teams[i] = "MEM"

	elif teams[i] == "Charlotte Hornets":
		teams[i] = "CHO"

	elif teams[i] == "Dallas Mavericks":
		teams[i] = "DAL"

	else: # "Chicago Bulls"
		teams[i] = "CHI"

# assemble game dicts
games = []
for i in range(len(teams)):
	if i % 2 == 0: # so for only for every pair of items
		temp_dict = {}
		temp_dict["AwayTeam"] = teams[i]
		temp_dict["HomeTeam"] = teams[i + 1]

		# calculte O/U margin
		if lines[i] >= 0:
			temp_dict["O/UMargin"] = (final_scores[i] + final_scores[i + 1]) - lines[i]
			temp_dict["HomeCoverBy"] = (final_scores[i + 1] - final_scores[i]) + lines[i + 1]
		else:
			temp_dict["O/UMargin"] = (final_scores[i] + final_scores[i + 1]) - lines[i + 1]
			temp_dict["HomeCoverBy"] = (final_scores[i + 1] - final_scores[i]) - lines[i]

		games.append(temp_dict)


print(games)


		
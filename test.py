from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# load page
html = urlopen("http://www.donbest.com/nba/odds/20160225.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

table = bsObj.find("table")

# scrape info
teams = table.findAll("span", {"class":"oddsTeamWLink"})
final_scores = table.findAll("div", {"id":re.compile("_Div_Score_.*")})
lines = table.findAll("div", {"id":re.compile("_Div_Line_.*_23$")})

# remove tags
teams = [team.text for team in teams]
final_scores = [float(final.text) for final in final_scores]
lines = [float(line.text) for line in lines]

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
		
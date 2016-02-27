from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.donbest.com/nba/odds/20160225.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

data = []
table = bsObj.find("table")



# get team name
for team in table.findAll("span", {"class":"oddsTeamWLink"}):
	print(team.text)

# get final score
for final in table.findAll("div", {"id":re.compile("_Div_Score_.*")}):
	print(final.text)

# get Mirage line
for line in table.findAll("div", {"id":re.compile("_Div_Line_.*_23$")}):
	print(line.text)
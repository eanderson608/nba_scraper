from sklearn.svm import SVR
import numpy as np
import json, os, math
import pickle



f = open("nba_stats_15_16_final.json")
game_file = [json.loads(line) for line in f]
f.close()

game_list = []
for di in game_file:
	if type(di) is not str:
		game_list.append(di)

ref_set = set()
team_set = set()


for game in game_list:
	team_set.add(game["HomeTeam"])
	for ref in game["Referees"]:
		ref_set.add(ref)

ref_list = list(ref_set)
team_list = list(team_set)
		
ref_list.sort()
team_list.sort()
print(ref_list)

f = open("ref_list.pkl", "wb")
pickle.dump(ref_list, f)
f.close()

f = open("team_list.pkl", "wb")
pickle.dump(team_list, f)
f.close()

from sklearn.svm import SVR

import numpy as np
import json, os, math
from random import shuffle
import pickle
import pprint


def main():

	# open file and read lines
	f = open("nba_stats_15_16_final.json")
	game_file = [json.loads(line) for line in f]
	f.close()

	# remove error messages
	game_list = []
	for di in game_file:
		if type(di) is not str:
			game_list.append(di)

	# get training and testing data
	X_train, y_ou_train, y_ps_train, X_test, y_ou_test, y_ps_test = transform_data(game_list, .80)

	# create classifier fit the point spread data
	clf = SVR(C=1.0, epsilon=0.2, kernel="poly")
	clf.fit(X_train, y_ps_train)
	pred = clf.predict(X_test)
	print(pred, y_ps_test)

	# predict PS data
	score = clf.score(X_train, y_ps_train)
	print(score)

def transform_data(game_list, train_percentage):

	# get team and ref lists
	f = open("ref_list.pkl", "rb")
	ref_list = pickle.load(f)
	f.close()
	f = open("team_list.pkl", "rb")
	team_list = pickle.load(f)
	f.close()


	shuffle(game_list)
	X = []
	y_ou = []
	y_ps = []
	for row in range(len(game_list)):
		temp = []

		# fill with ref binaries
		for col in range(len(ref_list)):
			if ref_list[col] in game_list[row]["Referees"]:
				temp.append(1)
			else:
				temp.append(0)

		# fill with away and home team binaries
		for col in range(len(team_list)):
			if team_list[col] == game_list[row]["AwayTeam"]:
				temp.append(1)
			else:
				temp.append(0)

			if team_list[col] == game_list[row]["HomeTeam"]:
				temp.append(1)
			else:
				temp.append(0)

		# make label list
		y_ou.append(game_list[row]["O/UMargin"])
		y_ps.append(game_list[row]["HomePSCoverBy"])
		X.append(temp)

	"""
	for i in range(len(y_ps)):
		if y_ps[i] <= 0:
			y_ps[i] = 0
		else:
			y_ps[i] = 1

	for i in range(len(y_ou)):
		if y_ou[i] <= 0:
			y_ou[i] = 0
		else:
			y_ou[i] = 1
	"""

	num_data_points = len(game_list)
	split = math.floor(train_percentage * num_data_points)
	X_train = X[:split]
	X_test = X[split:]
	y_ou_train = y_ou[:split]
	y_ou_test = y_ou[split:]
	y_ps_train = y_ps[:split]
	y_ps_test = y_ps[split:]

	return X_train, y_ou_train, y_ps_train, X_test, y_ou_test, y_ps_test


if __name__ == "__main__":
	main()
def convert_team_names(teams):

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

		elif teams[i] == "Chicago Bulls":
			teams[i] = "CHI"

		else: # "Chicago Bulls"
			teams[i] = "ERROR BAD TEAM NAME"

	return teams
from datetime import *
from Tweetstream import *
from UserAnalyser import *
from TimeAnalyser import *
import math
import sys
import pickle
#Frequency over the common


if __name__ == "__main__":
	keywords = open(sys.argv[2], 'r').readline().strip("\n").split(",")
	userstream = Tweetstream(jsonfilee=sys.argv[3], jsonformat=False, keywords=keywords)
	topicstream = Tweetstream(jsonfilee=sys.argv[1], jsonformat=False, keywords=keywords)
	ua = UserAnalyser (sys.argv[4], keywords = keywords)
	ua.load_usersVectors()
	ua.load_idf()
	ua.load_usersScore()
	rank = dict()
	
	ntweets = dict()
	for t in userstream:
		if not(t['user_id'] in ntweets): ntweets[t['user_id']] = 1
		else: ntweets[t['user_id']] += 1

	# normalizar pelo numero de kw no topic vector
	for t in userstream:
		score = 0.0
		if t['user_id'] in ua.usersScore:
			rank[t['id']] = (ua.usersScore[t['user_id']]/ntweets[t['user_id']])
		#prinit score, nwindow
	pickle.dump(rank, open(sys.argv[4]+"_rank_USER_usNorm.pick", 'w'), pickle.HIGHEST_PROTOCOL)

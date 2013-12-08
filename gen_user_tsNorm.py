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
	tw = TimeAnalyser(userstream=userstream, topicstream=topicstream, userinfo=ua)
	nwindow = 0
# normalizar pelo numero de kw no topic vector

	for (userwindow, topicwindow) in tw:
		users = set()
		for t in topicwindow:
			users.add(t['user_id'])

		for t in userwindow:
			score = 0.0
			if t['user_id'] in ua.usersScore:
				rank[t['id']] = ua.usersScore[t['user_id']]/math.log(len(users))
			#prinit score, nwindow
	pickle.dump(rank, open(sys.argv[4]+"_rank_USER_tsNorm.pick", 'w'), pickle.HIGHEST_PROTOCOL)

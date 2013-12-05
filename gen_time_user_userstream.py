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
	tw = TimeAnalyser(userstream=userstream, topicstream=topicstream, userinfo=ua)
	nwindow = 0
	rank = dict()
	
	ntweets_perUser = dict()
	for t in userstream:
		if t['user_id'] in ntweets_perUser: ntweets_perUser[t['user_id']] += 1
		else: ntweets_perUser[t['user_id']] = 1
	print "Freq per user computed"
	for (userwindow, topicwindow) in tw:
		score = 0.0
		users = set()
		
		temp = True	
		for t in userwindow:
			if temp:
				temp = False
				print t['created_at'] + '\t',
			users.add(t['user_id'])
		
		nusers = len(users)
		for user in users:
			if user in ua.usersScore:
				score += ua.usersScore[user]/(1.0 + math.log(ntweets_perUser[user]))
			else:
				nusers -= 1
		score /= nusers
		print score
		for t in userwindow:
			rank[t['id']] = score
		#prinit score, nwindow
	pickle.dump(rank, open(sys.argv[4]+"_rank_TIME_users_ustream.pick", 'w'), pickle.HIGHEST_PROTOCOL)

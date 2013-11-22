from datetime import *
from Tweetstream import *
from UserAnalyser import *
from TimeAnalyser import *
import math
import sys

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
	rank = []
	for (userwindow, topicwindow) in tw:
		score = 0.0
		keyword_frequencies = dict()
		for kw in keywords:
			keyword_frequencies[kw] = 0
			
		for t in topicwindow:
			for kw in keywords:
				if kw in t['text']:
					keyword_frequencies[kw] += 1
		
		for kw in keywords:
			score += ((1.0 + math.log(keyword_frequencies[kw])/math.log(2)) * ua.idf[kw])	
		score /= len(topicwindow)

		for t in userwindow:
			rank.append((score, t))
	#	for t in a:
	#		print t['created_at']
	#	for t in b:
	#		print t['created_at']
		print score, nwindow
	sorted(rank)
	for (i, t) in enumerate(rank):
		if i == 50: break
		print t

from datetime import *
from Tweetstream import *
from UserAnalyser import *
from TimeAnalyser import *
import math
import sys

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
	for (a, b) in tw:
		nwindow += 1
		print len(a), len(b)
		#for t in a:
	#		print t['created_at']
	#	for t in b:
	#		print t['created_at']
		print nwindow

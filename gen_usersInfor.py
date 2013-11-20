from UserAnalyser import *
from Tweetstream import *
import sys

l = [119372344, 44175574, 126477271, 252422812, 26299276, 560049049, 388473707, 1217370608, 842373594, 139960190, 45584847, 63573676, 274629513, 94176291, 68545824, 98997286, 139177492, 14201313, 118852899, 269567535]

if __name__ == "__main__":
	keywords = open(sys.argv[3], 'r').readline().strip("\n").split(",")
	ts = Tweetstream (jsonfilee=sys.argv[2], jsonformat=False, keywords=keywords)
	ua = UserAnalyser (sys.argv[1], tweetstream=ts)
	ua.compute_usersVectors()
	ua.compute_idf()
	ua.compute_usersScore()
#	for u in l:
#		print ua.usersVectors[u]
#		print ua.usersScore[u]

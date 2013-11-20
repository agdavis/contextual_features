from UserAnalyser import *
from Tweetstream import *
import sys

if __name__ == "__main__":
	keywords = open(sys.argv[3], 'r').readline().strip("\n").split(",")
	ts = Tweetstream (jsonfilee=sys.argv[2], jsonformat=False, keywords=keywords)
	ua = UserAnalyser (sys.argv[1], tweetstream=ts)
	ua.compute_usersVectors()

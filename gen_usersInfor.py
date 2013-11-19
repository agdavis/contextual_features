from UserAnalyser import *
from Tweetstream import *
import sys

if __name__ == "__main__":
	Tweetstream ts(sys.argv[2])
	UserAnalyser ua(sys.argv[1], tweetstream=ts)
	ua.compute_userVectors()

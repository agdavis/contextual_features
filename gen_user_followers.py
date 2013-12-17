from datetime import *
from Tweetstream import *
from UserAnalyser import *
from TimeAnalyser import *
import math
import sys
import pickle
#Frequency over the common

def load_list(filein):
	d = dict()
	for l in filein:
		l = eval(l)
		d[l[0]] = l[1]
	return d


if __name__ == "__main__":
	follow = load_list(open(sys.argv[5], 'r'))
	keywords = open(sys.argv[2], 'r').readline().strip("\n").split(",")
	userstream = Tweetstream(jsonfilee=sys.argv[3], jsonformat=False, keywords=keywords)
	topicstream = Tweetstream(jsonfilee=sys.argv[1], jsonformat=False, keywords=keywords)
	ua = UserAnalyser (sys.argv[4], keywords = keywords)
	
	ua.load_usersVectors()
	ua.load_idf()
	ua.load_usersScore()
	rank = dict()

	# normalizar pelo numero de kw no topic vector
	c = 0
	for t in userstream:
		rank[t['id']] = 0
		n = 0
		if t['user_id'] in follow:
			c += 1
			for fuser in follow[t['user_id']]:
				if fuser in ua.usersScore:
					rank[t['id']] += ua.usersScore[fuser]
					n += 1
		if n > 0: rank[t['id']] /= n
	print c
		#prinit score, nwindow
	pickle.dump(rank, open(sys.argv[4]+"_rank_USER_followers.pick", 'w'), pickle.HIGHEST_PROTOCOL)

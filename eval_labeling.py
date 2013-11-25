import random
import math
import sys
import pickle
#Frequency over the common


if __name__ == "__main__":
	validation_file = open(sys.argv[1], 'r')
	labeled_file = open(sys.argv[2], 'w')
	tweets = []
	for t in validation_file:
		tweets.append(eval(t))
	
	npositive = 0
	labeled = []
	random.shuffle(tweets)
	i = 0 
	while npositive < 100:
		print tweet[i]
		ans = raw_input()
		while ans != 'NFL' or ans != 'MLB' or ans != 'NBA' or ans != 'NHL' or ans != 'NONE': ans = raw_input()
		tweet[i]['label'] = ans
		labeled.append(tweet)
		pickle.dump(labeled, labeled_file, pickle.HIGHEST_PROTOCOL)
		

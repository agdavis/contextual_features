import random
import math
import sys
import pickle
#Frequency over the common


if __name__ == "__main__":
	validation_file = open(sys.argv[1], 'r')
	tweets = []
	for t in validation_file:
		tweets.append(eval(t))
	
	npositive = 0
	labeled = []
	random.shuffle(tweets)
	i = 0 
	while npositive < 100:
		print tweets[i]
		ans = raw_input().strip('\n')
		while not (ans != 'NFL' or ans != 'MLB' or ans != 'NBA' or ans != 'NHL' or ans != 'NONE'): ans = raw_input().strip('\n')
		if ans == 'MLB': npositive += 1
		tweets[i]['label'] = ans
		labeled.append(tweets[i])
		pickle.dump(labeled, open(sys.argv[2], 'w'), pickle.HIGHEST_PROTOCOL)
		i += 1	

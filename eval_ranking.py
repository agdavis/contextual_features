import random
import math
import sys
import pickle
from operator import itemgetter
#Frequency over the common

"""
Calculate mean and standard deviation of data x[]:
    mean = {\sum_i x_i \over n}
    std = sqrt(\sum_i (x_i - mean)^2 \over n-1)
"""
def meanstdv(x):
    from math import sqrt
    n, mean, std = len(x), 0, 0
    for a in x:
	mean = mean + a
    mean = mean / float(n)
    for a in x:
	std = std + (a - mean)**2
    std = sqrt(std / float(n-1))
    return mean, std

if __name__ == "__main__":
	rank = pickle.load(open(sys.argv[1], 'r'))
	labeled = pickle.load(open(sys.argv[2], 'r'))
	label = sys.argv[3]
	users = eval(open("/scratch/agdavis/usersCollection.txt", 'r').readline())
	N = 100
	nrep = 50
	
	hits = []
	nPositive = 0
	for i in xrange(0, N+1):
		hits.append([])
	for rep in xrange(0, nrep):
		res = []
		for ltweet in labeled:
			if ltweet['label'] == label and rank[ltweet['id']] > 0 :
				if rep == 0: nPositive += 1 # Counts the number of labeled examples
				population = random.sample(rank.items(), N)
				population.append((ltweet['id'], rank[ltweet['id']]))
				population = sorted(population, key=itemgetter(1), reverse=True)
				for (i, t) in enumerate(population):
					if (t[0] == ltweet['id']):
						res.append(i)
						break
		res = sorted(res)
		#print res
		for i in xrange(0, N+1):
			hits[i].append(sum([ k <= i for k in res]))
	
	
	print "No hits"
	mean_stddev = [meanstdv(x) for x in hits]
	for (i, (mean, stddev)) in enumerate(mean_stddev):
		print i, '\t', mean, '\t', stddev
	
	print "precision recal"
	prec_recal = [(x[0]/(nPositive*(n+1)), (x[0]/nPositive)) for (n, x) in enumerate(mean_stddev)]
	for (i, (prec, rec)) in enumerate(prec_recal):
		print i, '\t', rec, '\t', prec

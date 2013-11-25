import random
import math
import sys
import pickle
#Frequency over the common


if __name__ == "__main__":
	rank = pickle.load(open(sys.argv[1]+"_rank_users_tstream.pick", 'r'))
	labeled = pickle.load(open(sys.argv[2]+"_rank_users_tstream.pick", 'r'))
	label = "MLB"

	# normalizar pelo numero de kw no topic vector
	res = []
	for ltweet in labeled:
		if ltweet['label'] == label:
			population = random.sample(rank.items(), 1000)
			population.append((ltweet['id'], rank[ltweet['id']]))
			sorted(population, key=lambda x: x[1], reverse=True)
			for (i, t) in population:
				if (t == ltweet['id']):
					res.append(i)
					break
			

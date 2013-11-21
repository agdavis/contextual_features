import cjson
import sys
import pickle
from datetime import *
from Tweetstream import *
import math

class UserAnalyser:
	def __init__(self, userFilePrefix, tweetstream=None, keywords=[]):
		self.usersVectors = dict()
		self.idf = dict()
		self.userScore = dict()
		if tweetstream: self.keywords = tweetstream.keywords
		else: self.keywords = keywords
		self.userFilePrefix = userFilePrefix
		self.tweetstream = tweetstream


	def __iter__(self):
		for l in self.usersVectors.iteritems():
			try:
				yield l
			except:
				continue

	def compute_usersVectors(self):
		i = 0
		for t in self.tweetstream:
			i += 1
			if i%50000 == 0:
				print i
			if t['user_id'] not in self.usersVectors:
				self.usersVectors[t['user_id']] = dict()
			for kw in self.keywords:
				if kw in t['text']:
					if not self.usersVectors[t['user_id']].has_key(kw):
						self.usersVectors[t['user_id']][kw] = 0
					self.usersVectors[t['user_id']][kw] += 1
		pickle.dump(self.usersVectors, open(self.userFilePrefix+"_usersVectors.pick", 'w'), pickle.HIGHEST_PROTOCOL)
		
				
	def compute_idf(self):
		self.idf = dict()
		#init
		for kw in self.keywords:
			self.idf[kw] = 0

		i = 0
		for (userid, uservector) in self:
			for word in uservector:
				self.idf[word] += 1
		print self.idf			
		for kw in self.keywords:
			if (self.idf[kw] > 0):
				self.idf[kw] = math.log( 1 + (len(self.usersVectors)/self.idf[kw]))/math.log(2)
		
		pickle.dump(self.idf, open(self.userFilePrefix+"_idf.pick", 'w'), pickle.HIGHEST_PROTOCOL)


	def compute_usersScore(self):
		self.usersScore = dict()
		for (userid, uservector) in self:
			score = 0.0
			for kw in uservector:
				freq = uservector[kw]
				score += (1.0 + math.log(freq)/math.log(2)) *self.idf[kw]
			self.usersScore[userid] = score
		pickle.dump(self.usersScore, open(self.userFilePrefix+"_usersScore.pick", 'w'), pickle.HIGHEST_PROTOCOL)

	
	def load_idf(self, filen=""):
		if not filen:
			self.idf = pickle.load(open(self.userFilePrefix+"_idf.pick", 'r'))
		else:
			self.idf = pickle.load(open(filen, 'r'))
			
	def load_usersScore(self, filen=""):
		if not filen:
			self.usersScore = pickle.load(open(self.userFilePrefix+"_usersScore.pick", 'r'))
		else:
			self.usersScore = pickle.load(open(filen, 'r'))
	
	def load_usersVectors(self, filen=""):
		if not filen:
			self.usersVectors = pickle.load(open(self.userFilePrefix+"_usersVectors.pick", 'r'))
		else:
			self.usersVectors = pickle.load(open(filen, 'r'))
		
if __name__ == "__main__":
	print "Lendo os usuarios" 
	u = UserAnalyser(sys.argv[1])
	print "Usuarios lidos"  
	#ts.users_vectors(sys.argv[3])
	ts.project_stream_features(["id", "user", "created_at", "text"], sys.argv[3])
	#ts.volume_per_hour()
	

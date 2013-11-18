import cjson
import sys
from datetime import *

#Input file format (user_id, keywords={})

class UserAnalyser:
	def __init__(self, userfile, keywords=[]):
		self.userlist = []
		self.useffile = userfile
		# Set init and end time
		userfile = open(userfile, "r")
		
		for user in self:
			self.userlist.append(user)

	def __iter__(self):
		json = open(self.userfile, "r")
		for l in json:
			try:
				yield eval(l)
			except:
				continue
				
	def overall_freq(self):
		self.words_overall_freq = dict()
		for user in userlist:
			for (word, count) in user[1].items():
				self.words_overall_freq[word] += count
	
				
			
		
			
			
				
		
		
if __name__ == "__main__":
	print "Lendo os usuarios" 
	u = UserAnalyser(sys.argv[1])
	print "Usuarios lidos"  
	#ts.users_vectors(sys.argv[3])
	ts.project_stream_features(["id", "user", "created_at", "text"], sys.argv[3])
	#ts.volume_per_hour()
	

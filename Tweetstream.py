import cjson
import sys
from datetime import *

def get_user(json):
	d = dict()
	d["user_id"] = json["user"]["id"]
	d["user_name"] = json["user"]["screen_name"]
	return d

class Tweetstream:
	def __init__(self, jsonfilee, keywords=[], jsonformat=True):
		self.jsonfilename = jsonfilee 
		self.jsonformat = jsonformat
		
		# Set init and end time
		json = open(jsonfilee, "r")
		tweet = self.decode_line(json.readline())
			
		self.inittime = datetime.strptime(tweet["created_at"], "%a %b %d %X +0000 %Y")
		
		lastLine = ""
		for l in json:
			lastLine = l
		tweet = self.decode_line(lastLine)
		self.endtime = datetime.strptime(tweet["created_at"], "%a %b %d %X +0000 %Y")
		
		print keywords
		self.keywords = keywords

	def __iter__(self):
		json = open(self.jsonfilename, "r")
		for l in json:
			try:
				yield self.decode_line(l)
			except:
				continue
	
	def decode_line(self, line):
		if (self.jsonformat):
			return cjson.decode(line)
		else:
			return eval(line)
			
	def detect_keyword(self, word):
		if (word in self.keywords):
			return word
		if (word[0] == '#' or word[0] == '@'):
			if (word[1:] in self.keywords):
				return word[1:]
		return ""
		
		
		
	
	def volume_per_hour(self):
		volume = dict()
		line = 1
		for tweet in self:
			try:
				mon = datetime.strptime(tweet["created_at"], "%a %b %d %X +0000 %Y").month
				day = datetime.strptime(tweet["created_at"], "%a %b %d %X +0000 %Y").day
				hour = datetime.strptime(tweet["created_at"], "%a %b %d %X +0000 %Y").hour
			except:
				print line
				continue
			mon = str(mon)
			day = str(day)
			hour = str(hour)
			if (len(mon) < 2):
				mon = '0'+mon
			if (len(day) < 2):
				day = '0'+day
			if (len(hour) < 2):
				hour = '0'+hour
			key = mon+day+hour
			
			if (not volume.has_key(key)):
				volume[key] = 1
			else:
				volume[key] += 1
			line += 1
		keys = sorted(volume.keys())
		for k in keys:
			print k, volume[k]
	
	# removes unuseful tags of json (Performance)		
	def project_stream_features(self, features = [], outputfile="out_stream.json", keywordText=False):
		outjson = open(outputfile, "w")
		for tweet in self:
			tweetout = dict()
			
			try:
				for f in features:
					if (f == 'text' and keywordText):
						tweetout[f] = self.project_text(tweet[f])
					elif(f == 'user'):
						#print get_user(tweet)
						tweetout.update(get_user(tweet))
					else:
						tweetout[f] = tweet[f]
			except:
				continue
			print >> outjson, tweetout
	
	 
	def project_text (self, text):
		words = text.split()
		ntext = ""
		for word in words:
			kword = self.detect_keyword(word)
			if( kword != ""):
				ntext += kword + ' '
		return ntext
		
	def users_vectors(self, outputfile):
		out = open(outputfile, "w")
		users = dict()
		for tweet in self:
			for kword in self.keywords:
				#kword = self.detect_keyword(word)
				if (kword in tweet["text"]):
					if not users.has_key(tweet["user_id"]):
						users[tweet["user_id"]] = dict()
						for k in self.keywords:
							users[tweet["user_id"]][k] = 0	
					users[tweet["user_id"]][k] += 1
		for u in users.items():
			print >> out, u
			
		
			
			
				
		
		
if __name__ == "__main__":
	print "Criando o stream"
	#ts = Tweetstream(sys.argv[1], open(sys.argv[2]).readline().split(","))
	ts = Tweetstream(sys.argv[1])
	print "Criado o stream"  
	#ts.users_vectors(sys.argv[3])
	ts.project_stream_features(["id", "user", "created_at", "text"], sys.argv[2])
	#ts.volume_per_hour()
	

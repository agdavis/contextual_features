import cjson
import sys
import pickle
from datetime import *
from Tweetstream import *
from UserAnalyser import *
import math

class TimeAnalyser:
	def __init__(self, keywords = [], userstream=None, topicstream=None, userinfo=None):
		self.keywords = keywords
		self.userstream = userstream
		self.topicstream = topicstream
		self.userinfo = userinfo
		
		self.windowSize = timedelta (hours=1)
		print userstream.inittime
		self.timeWindowInit = userstream.inittime.replace(minute = 0, second = 0)
		self.timeWindowEnd = self.timeWindowInit + self.windowSize
		print self.timeWindowInit, self.timeWindowEnd

		self.tempWindowUser = []
		self.tempWindowTopic = []

	def __iter__(self):
		self.userstreamit = iter(self.userstream)
		self.topicstreamit = iter(self.topicstream)
		over = False
		while (not over):
			twWindowUser = []
			twWindowTopic = []
			twWindowUser += self.tempWindowUser
			twWindowTopic += self.tempWindowTopic
			self.tempWindowUser = []
			self.tempWindowTopic = []
			for t in self.userstreamit:
				if convert_time(t["created_at"]) < self.timeWindowInit: continue
				if convert_time(t["created_at"]) >= self.timeWindowEnd:
					self.tempWindowUser.append(t)
					break
				twWindowUser.append(t)
			else:
				over = True


			for t in self.topicstreamit:
				#print t["created_at"], self.timeWindowInit
				if convert_time(t["created_at"]) < self.timeWindowInit: continue
				if convert_time(t["created_at"]) >= self.timeWindowEnd:
					self.tempWindowTopic.append(t)
					break
				twWindowTopic.append(t)
			else:
				over = True

			#update window
			self.timeWindowInit = self.timeWindowEnd
			self.timeWindowEnd = self.timeWindowInit + self.windowSize
			
			# Consume the rest of the stream
			if (over):
				for t in self.userstreamit: continue
				for t in self.topicstreamit: continue
			yield (twWindowUser, twWindowTopic)
			
		

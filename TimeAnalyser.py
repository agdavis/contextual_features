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

		self.userstreamit = iter(self.userstream)
		self.topicstreamit = iter(self.topicstream)
		self.tempWindowUser = []
		self.tempWindowTopic = []

	def __iter__(self):
		twWindowUser = []
		twWindowTopic = []
		twWindowUser += self.tempWindowUser
		twWindowTopic += self.tempWindowTopic
		self.tempWindowUser = []
		self.tempWindowTopic = []

		for t in self.userstreamit:
			if t["created_at"] < self.timeWindowInit: continue
			if t["created_at"] >= self.timeWindowEnd:
				self.tempWindowUser.append(t)
				break
			twWindowUser.append(t)
			
		for t in self.topicstreamit:
			if t["created_at"] < self.timeWindowInit: continue
			if t["created_at"] >= self.timeWindowEnd:
				self.tempWindowTopic.append(t)
				break
			twWindowUserTopic.append(t)
		self.timeWindowInit = self.timeWindowEnd
		self.timeWindowEnt += self.windowSize
		yield (twWindowUser, twWindowTopic)
			
		

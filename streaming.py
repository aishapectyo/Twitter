#!/usr/bin/env python

import sys
import os
import numpy as np
import scipy
import matplotlib.pyplot as plt
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter as tt

#---Your access keys go here---#
access_token = "your access token goes here"
access_token_secret = "your access token secret goes here"
consumer_key = "your consumer key goes here"
consumer_secret = "your consumer secret goes here"

class StdOutListener(StreamListener):
	def on_data(self, data):
		print data
		FO.write(data)
		return True

	def on_error(self, status):
		print status

if __name__ == '__main__':
	
	FO = open("twitter_data.txt","w")
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	stream.filter(track=['knitting', 'crochet', 'cross stitch', 'sewing', 'diy'])
	#clearly I am using crafting keywords here, change them to what you need them to be
	

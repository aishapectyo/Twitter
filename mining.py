#!/usr/bin/env python

import sys
import os
import numpy as np
import scipy
import matplotlib.pyplot as plt
import json
import unicodedata
from collections import Counter

#---Read Data----#
data_path = 'path to your data goes here'
tweets_data = []
tweets_file = open(data_path, "r")
print('converting tweets to json format...')
for line in tweets_file:
	try:
		single_tweet = json.loads(line)
		#append json formatted tweet into an array
		#data type will be a dictionary
		tweets_data.append(single_tweet)
	except:
		continue

print len(tweets_data) #check how many tweets we have

#check that each tweet has the keyword we are interested in.
#essentially, filter out those tweets WITHOUT the keyword.
tweet = tweets_data[0] #access ONE tweet.
keyword_text = 'text'
keyword_coords = 'geo'
keyword_language = 'lang'
tweet_text=[]
tweet_coords=[]
tweet_lang=[]
print('checking for keywords...')
for tweet in tweets_data:
	if keyword_text in tweet:
		tweet_text.append(tweet['text'])
	if keyword_coords in tweet:
		tweet_coords.append(tweet['geo'])
	if keyword_language in tweet:
		tweet_lang.append(tweet['lang'])
#new length of our tweets
print len(tweet_text)
print len(tweet_coords)
print len(tweet_lang)


#check how many tweets you have per language
count_ocurrances = Counter(tweet_lang).most_common() #creates list of tuples in decreasing order 
#we want to access each character separately
#this is called a list comprehension
comp1 = [x[0] for x in count_ocurrances]
language_frequency =  [x[1] for x in count_ocurrances]

#change unicode to ascii
language_id = []
for j in xrange(len(count_ocurrances)):
	notuni =  unicodedata.normalize('NFKD', comp1[j]).encode('ascii','ignore')
	language_id.append(notuni) 

#check for specific keywords in your tweets. 
craft1 = 'knitting'
craft2 = 'crochet'
craft3 = 'cross stitch'
craft4 = 'sewing'
craft5 = 'diy'
#counter to check frequency
counter1=0
counter2=0
counter3=0
counter4=0
counter5=0
counter6=0
counter7=0
counter8=0
counter9=0
text = tweet_text[0]
print('check frequency of crafts...')
for text in tweet_text:
	if craft1 in text:
		counter1 = counter1 + 1
	if craft2 in text:
		counter2 = counter2 + 1
	if craft3 in text:
		counter3 = counter3 + 1
	if craft4 in text:
		counter4 = counter4 + 1
	if craft5 in text:
		counter5 = counter5 + 1
	if craft1 and 'old' in text:
		counter6 = counter6 + 1
	if craft1 and 'cat' in text:
		counter7 = counter7 + 1
	if craft1  and 'fun' in text:
		counter8 = counter8 + 1
	if craft1 and 'wine' in text:
		counter9 = counter9 + 1
	
#get a few percentages
total = len(tweet_text)
knit_percentage = float(counter1)/total * 100
crochet_percentage = float(counter2)/total * 100
cross_percentage = float(counter3)/total * 100
sewing_percentage = float(counter4)/total * 100
diy_percentage = float(counter5)/total * 100
knitold_percentage = float(counter6)/counter1 * 100
knticat_percentage = float(counter7)/counter1 * 100
knitfun_percentage = float(counter8)/counter1 * 100
knitwine_percentage = float(counter9)/counter1 * 100
#create array with all your data values
crafts = [craft1, craft2, craft3, craft4, craft5, 'old', 'cat', 'fun', 'wine']
counters = [counter1, counter2, counter3, counter4, counter5, counter6, counter7, counter8, counter9]
percentages = [knit_percentage, crochet_percentage, cross_percentage, sewing_percentage, diy_percentage, knitold_percentage, knticat_percentage, knitfun_percentage, knitwine_percentage]

#save numbers to a file
new_file = open('results_crafts.txt', 'w')
#make a header
print >> new_file, 'craft, number of tweets, percentage'

array_len = len(crafts)
for x in xrange(array_len):
	counters[x] = str(counters[x])
	percentages[x] = str(percentages[x])
	new_file.write(crafts[x]+' '+counters[x]+' '+percentages[x]+'\n')
new_file.close()
	
new_file2 = open('results_lang.txt', 'w')
print >> new_file2, 'language id, language frequency'
array_len2 = len(language_id)
for j in xrange(array_len2):
	language_frequency[j] = str(language_frequency[j])
	new_file2.write(language_id[j]+' '+language_frequency[j]+'\n')
new_file2.close()
print('files written succesfully.')

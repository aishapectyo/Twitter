#!/usr/bin/env python

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import csv
import plotly.plotly as py 
import plotly.tools as tls
from plotly.graph_objs import *

#----Read Data----#
craft=[]
number_tweets=[]
percentage=[]

with open('results_crafts.txt', 'r') as f:
	header_line = next(f)
	reader = csv.reader(f, delimiter=' ')
	for row in reader:
		craft.append(row[0])
		int1 = int(row[1])
		number_tweets.append(int1)
		float1 = float(row[2])
		percentage.append(float1)


language_id=[]
language_count=[]
with open('results_lang.txt', 'r') as f2:
	header_line = next(f2)
	reader = csv.reader(f2, delimiter=' ')
	for row in reader:
		language_id.append(row[0])
		int2 = int(row[1])
		language_count.append(int2)


#---Plot---#

#Number of Tweets per Craft
data = Data([Bar(x=['Knitting', 'Crochet', 'Cross Stitch', 'Sewing', 'DIY'],y=[number_tweets[0], number_tweets[1], number_tweets[2], number_tweets[3], number_tweets[4]], marker=Marker(color='rgb(142, 124, 195)'))])
layout = Layout(title='Number of Tweets per Craft',font=Font(family='Raleway, sans-serif'),showlegend=False,xaxis=XAxis(tickangle=-45),yaxis=YAxis(zeroline=False,gridwidth=2),bargap=0.05)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='tweetspercraft')

#Number of Tweets per Language
data2 = Data([Bar(x=['English', 'Japanese', 'Indonesian', 'Spanish', 'French', 'German'],y=[language_count[0], language_count[1], language_count[2], language_count[3], language_count[4], language_count[5]], marker=Marker(color='#8DB6CD'))])
layout = Layout(title='Number of Tweets per Language',font=Font(family='Raleway, sans-serif'),showlegend=False,xaxis=XAxis(tickangle=-45),yaxis=YAxis(zeroline=False,gridwidth=2),bargap=0.05)
fig = Figure(data=data2, layout=layout)
plot_url = py.plot(fig, filename='tweetsperlang')

#Knitting in Relation to Other Keywords
trace1 = Scatter(x=['Old', 'Cat', 'Fun', 'Wine'], y=[number_tweets[5], number_tweets[6], number_tweets[7], number_tweets[8]],mode='markers', marker=Marker(color=['#95B9C7', '#667C26', '#F75D59', '#7D1B7E'],size=[102, 62, 32, 12],opacity=[0.6, 0.7, 0.8, 0.9]))
data3 = Data([trace1])
layout = Layout(title='Number Tweets Related to Knitting and Other Keywords',font=Font(family='Raleway, sans-serif'),showlegend=False)
fig = Figure(data=data3, layout=layout)
plot_url = py.plot(fig, filename='bubbleskeywords')

#What have I knitted?
data4 = Data([Bar(x=['Shawls', 'Hats', 'Mittens', 'Socks', 'Sweaters', 'Other'],y=[15, 4, 5, 2, 3, 3], marker=Marker(color='#E77471', opacity=(0.7, 0.7, 0.7, 0.7,0.7,0.7)))])
layout = Layout(title='What Have I knitted?',font=Font(family='Raleway, sans-serif'),showlegend=False,xaxis=XAxis(tickangle=-45),yaxis=YAxis(zeroline=False,gridwidth=2),bargap=0.05)
fig = Figure(data=data4, layout=layout)
plot_url = py.plot(fig, filename='my knit')


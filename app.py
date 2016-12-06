"""A simple way of getting timeline Tweets and plot them using Python and D3"""


__author__ = "Jose Herrerías"
__version__ = "1.0.0"
__email__ = "herreriasjose@gmail.com"
__status__ = "Test"


import json
import os
import sys
import webbrowser

from collections import Counter
from datetime import datetime
from simple_server import Simple_server
from time import sleep
from twitter_get_user_timeline import get_user_timeline
from urllib.request import pathname2url

	
	

def extract_data(tweet):
	date = tweet.get('created_at',[])
	date_object = datetime.strptime(date,'%a %b %d %H:%M:%S +0000 %Y')
	date_object = date_object.replace(hour=0, minute=0, second=0, microsecond=0)
	date = date_object.strftime('%Y-%m-%d')
	entities = tweet.get('entities',{})
	hashtags = entities.get('hashtags',[])
	hashtags_list = []
	for tag in hashtags:
		hashtags_list.append(tag['text'].lower());
	
	dateDic = {'created_at':date,'hashtags':hashtags_list}
	return(dateDic)


if __name__ == '__main__':
	
	user_name = input('User name?: ')
	
	
	if (not get_user_timeline(user_name)):
		# Problems with Oauth?
		print("Error:")
		print("Have you introduced your API key, API secret, etc. properly?")
		sys.exit()
		
	print("Extracting data...")
	
	dates_list = []
	fname = 'user_timeline_{}.jsonl'.format(user_name)
			
	
	with open(fname,'r') as f:
		for line in f:
			tweet = json.loads(line)
		
			dates_list.append(extract_data(tweet))
	
	
	dates_list.sort(key=lambda d: d['created_at'])
	
	a_day = []
	for x in dates_list:
		a_day.append(x['created_at'])
	
	unique_days = Counter(a_day)
	
	unique_days = list(unique_days.items())
	
	data = []
	for u in unique_days:
		hashtags = []
		for d in dates_list:
			if (u[0] == d['created_at']):
				if (d['hashtags']):
					for h in d['hashtags']:
						hashtags.append(h)
		
		datum = {'created_at':u[0],'tweets':u[1],'hashtags':hashtags}
		data.append(datum)
		
	
	data.sort(key=lambda d: d['created_at'])	
	with open('tweets_dataset.json','w') as f:
		json.dump(data,f)
		
	print("Done.")
	s = Simple_server()
	s.start()
	sleep(2)
	print("Showing plot...")
	webbrowser.open("http://127.0.0.1:8080/index.html")
	print("Done.")
	
	


		

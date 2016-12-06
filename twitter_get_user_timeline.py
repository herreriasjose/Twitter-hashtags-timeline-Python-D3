import itertools
import sys
import json
from datetime import datetime
from tweepy import Cursor
from twitter_client import get_twitter_client


spinner = itertools.cycle(['-', '\\', '|','/' ])


def get_user_timeline(user):

	
	fname= 'user_timeline_{}.jsonl'.format(user)
	client = get_twitter_client()
	print("Downloading timeline...")
	try:
		with open(fname,'w') as f:
			for page in Cursor(client.user_timeline, screen_name= user, count=200).pages(16):
				sys.stdout.write(spinner.__next__())
				sys.stdout.flush()                
				sys.stdout.write('\b')            
				for status in page:
					f.write(json.dumps(status._json)+'\n')
			print("Done.")
		with open('user.json','w') as f:
			t = datetime.now()
			t = t.strftime("%A, %d. %B %Y %I:%M%p")
			data_user = {'user':user,'date': t}
			f.write(json.dumps(data_user))			
		return True
	except Exception as e:
			print("Error:")
			print(e) 
			return False
	
		



if __name__ == '__main__':
	
	
	user_name = input('User name?: ')
	get_user_timeline(user_name)
	
	
	


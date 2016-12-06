from tweepy import API
from tweepy import OAuthHandler
import sys


API_KEY =	"uszRU7CBLx5MhDx1lYpaFUxZM" # Consumer Key (API Key)
API_SECRET =	"dl8bzTdMfExRehPw9XhoSf2bDzix4xBQhK1zh3HuDV1QOVepwq" # Consumer Secret (API Secret)

TOKEN_KEY =		"2329449824-Vju5G1VzL2SzWQwEcToAIaeP1Mt3gu3ZyLiL2Xb" # Access Token
TOKEN_SECRET =	"irHMEBpYonWoyNH8qktF7ymPUlSz1mCNTE4qB9GtNVX7c" # Access Token Secret


def get_twitter_auth():

	try:
		auth = OAuthHandler( API_KEY,  API_SECRET)
		auth.set_access_token( TOKEN_KEY,  TOKEN_SECRET)
	except e:
		print("There's been an error with the Auth: ", e)
		sys.exit(1)
	return auth



def get_twitter_client():

	auth = get_twitter_auth()
	try:
		client = API(auth)
	except e:
		print("There's been an error with the Client: ", e)
		sys.exit(1)
	
	return client
	




if __name__ == "__main__":
	
	client = get_twitter_client()
	print(client)


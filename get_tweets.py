from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient
from IPython import embed
 
class StreamListener(tweepy.StreamListener):

    def on_connect(self):
        """Called when the connection is made"""
        print("You're connected to the streaming server.")
 
    def on_error(self, status_code):
        """This is called when an error occurs"""
        print('Error: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        """This will be called each time we receive stream data"""
        client = MongoClient('localhost', 27017)
 
        # Use cooldb database
        db = client.cooldb
 
        # Decode JSON
        datajson = json.loads(data)
        # embed()
        try:
            goodtweet = {}
            
            goodtweet['lang'] = datajson['lang']
            goodtweet['text'] = datajson['text']
            goodtweet['screen_name'] = datajson['user']['screen_name']
            
            print(goodtweet)
            
            db.cooltweets.insert(goodtweet)
        except:
            pass

 
# Path to the list of Emoji
STOPWORDS_PATH1 = 'emoji_stopwords1.txt'
STOPWORDS_PATH2 = 'emoji_stopwords2.txt'
STOPWORDS_PATH3 = 'emoji_stopwords3.txt'
STOPWORDS_PATH4 = 'emoji_stopwords4.txt'
STOPWORDS_PATH5 = 'emoji_stopwords5.txt'
STOPWORDS_PATH6 = 'emoji_stopwords6.txt'

#insert your own twitter api credentials here 
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""
 
#Authenticating
auth1 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth1.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
 
l = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth1, listener=l)
with open(STOPWORDS_PATH1) as f:
    streamer.filter(track=[word.strip().decode('utf-8') for word in f])
with open(STOPWORDS_PATH2) as f:
    streamer.filter(track=[word.strip().decode('utf-8') for word in f])
with open(STOPWORDS_PATH3) as f:
    streamer.filter(track=[word.strip().decode('utf-8') for word in f])
with open(STOPWORDS_PATH4) as f:
    streamer.filter(track=[word.strip().decode('utf-8') for word in f])
with open(STOPWORDS_PATH5) as f:
    streamer.filter(track=[word.strip().decode('utf-8') for word in f])
with open(STOPWORDS_PATH6) as f:
    streamer.filter(track=[word.strip().decode('utf-8') for word in f])

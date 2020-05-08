from __future__ import print_function
import json
from pymongo import MongoClient
from IPython import embed
import re

#regex to capture emoji
myre = re.compile(u'['
    u'\U0001F300-\U0001F64F'
    u'\U0001F680-\U0001F6FF'
    u'\u2600-\u26FF\u2700-\u27BF]+', 
    re.UNICODE)


client = MongoClient('localhost', 27017)

db = client.cooldb
#load tweets
tweets= db.cooltweets.find()

#iterate through tweets
for tweet in tweets:
	
	tweettext = tweet['text']
	emojis = myre.findall(tweettext)
	for emoji in emojis:
		lang = tweet['lang']
		#only use the relevant langues
		if lang == 'en' or lang == 'es' or lang == 'fr' or lang == 'de' or lang == 'zh' or lang == 'ru' or lang == 'ko' or lang == 'it' or lang == 'ja':
			#only if the emoji string is 4 chars or less
			if len(emoji)< 5:
				#increment the language number, and create record if it doesn't exist
				db.tweetcount.update(
					{ 'emoji' : emoji },
					{ '$inc': { lang : 1}},
					upsert=True)
		print(emoji)

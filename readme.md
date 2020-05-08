# Twitter Emoji Discovery Tools

This directory contains a number of files to help discover the frequency of emoji usage on Twitter. These were all pulled together pretty quickly, and probably wouldn't pass muster in a production environment, but provide a way to gather some quick and dirty insights.

They include:

- `get_tweets.py` - a Python script that uses the Twitter streaming API to capture the text and language of tweets using emojis, and then insert a record into a MongoDB collection with the tweet text and language.

- `emoji_stopwords1.txt` - `emoji_stopwords2.txt` - lists of emojis used by get_tweets.py

- `get_emoji.py` - a Python script that iterates through the Mongo collection created by running get_tweets.py, to create a new Mongo collection that allows the data to be analyzed. (I recommend running this in Python 3, because of how Python 3 handles Unicode; Python 2.7 may have issues using the regex to detect emojis in each tweet.) For each emoji or group of emojis, it uses Mongo's upsert functionality to either create a document or update the existing document, incrementing the number of times that emoji or emoji string has occured for a given language.

- `notes.py` - a few notes, including the regex used to identify emojis in the tweet text.

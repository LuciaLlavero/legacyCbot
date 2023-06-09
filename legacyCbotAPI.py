import tweepy
import numpy as np
import os
import json

#Variables for accessing twitter API
jsonKeys = open('keys.json', 'r')
keys = json.load(jsonKeys)

#Authenticating to access the twitter API
api = tweepy.Client(consumer_key=keys['consumerKey'],
                    consumer_secret=keys['consumerSecretKey'],
                    access_token=keys['accessToken'],
                    access_token_secret=keys['accessTokenSecret'])

#Getting the number of the next tweet stored in json file
jsonFile = open('numTweet.json', 'r')
data = json.load(jsonFile)
numTweet = data['increment']
#Updating the tweet number to the next
data['increment'] += 1
with open('numTweet.json', 'w') as file:
    json.dump(data, file)
jsonFile.close()

#Checking if the text file exist
textFileExist = False
if(os.path.exists('tweet_'+str(numTweet))):
    textFileExist = True

#Creating new tweet
if(textFileExist == True):
    textFile = open('tweet_'+str(numTweet), 'r')
    tweetText = textFile.read()
    textFile.close()
    api.create_tweet(text=tweetText)

jsonKeys.close()

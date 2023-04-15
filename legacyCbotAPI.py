import tweepy
import numpy as np
import os
import json

#Variables for accessing twitter API
jsonKeys = open('keys.json')
keys = json.load(jsonKeys)

#Authenticating to access the twitter API
api = tweepy.Client(consumer_key=keys['consumerKey'],
                    consumer_secret=keys['consumerSecretKey'],
                    access_token=keys['accessToken'],
                    access_token_secret=keys['accessTokenSecret'])

#Getting the number of the next tweet stored in json file
jsonFile = open('numTweet.json')
data = json.load(jsonFile)
numTweet = data['increment']

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

#Updating the tweet number to the next
numTweet += 1
jsonFile['increment'] = numTweet

#Closing files
jsonKeys.close()
jsonFile.close()

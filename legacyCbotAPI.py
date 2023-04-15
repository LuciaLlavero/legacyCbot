import tweepy
import numpy as np
import os
import json

#Variables for accessing twitter API
jsonKeysFile = open('keys.json')
keys = json.load(jsonKeysFile)

#Authenticating to access the twitter API
auth = tweepy.OAuthHandler(keys['consumerKey'], keys['consumerSecretKey'])
auth.set_access_token(keys['accessToken'], keys['accessTokenSecret'])
api = tweepy.API(auth)

#Getting the number of the next tweet stored in json file
jsonFile = open('numTweet.json')
data = json.load(jsonFile)
numTweet = data['increment']

#Checking if the text file exist
bool textFileExist = false
if(os.path.exist("./legacyCbot/tweet_"+str(numTweet)+".txt")):
    textFileExist = true

#Checking if the image exist
bool imageExist = false
if(os.path.exist("./legacyCbot/image_"+str(numTweet)+".jpg")):
    imagePath = "./legacyCbot/image_"+str(numTweet)+".jpg"
    imageExist = true

if(imageExist and textFileExist):
    with open('./legacyCbot/tweet_'+str(numTweet)+'.txt', 'r') as file:
        tweetText = file.read()
    #Generate text tweet with media (image)
    status = api.update_with_media(imagePath, tweetText)
    api.update_status(status=tweetText)
    os.remove("./legacyCbot/tweet_"+str(numTweet)+".txt")
    os.remove("./legacyCbot/image_"+str(numTweet)+".jpg")
else if(imageExist == false and textFileExist):
    with open('./legacyCbot/tweet_'+str(numTweet)+'.txt', 'r') as file:
        tweetText = file.read()
    #Generate text tweet without media (image)
    api.update_status(tweetText)
    os.remove("./legacyCbot/tweet_"+str(numTweet)+".txt")

#Updating the tweet number to the next
numTweet += 1
data['increment'].update(numTweet)

#Closing json files
jsonFile.close()
jsonKeys.close()
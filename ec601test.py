#!/usr/bin/env python
# encoding: utf-8
#Author - Shuhao Hu

import tweepy #https://github.com/tweepy/tweepy
import wget
import json

#Twitter API credentials


consumer_key = "nYEgZs6LnnNLSd8iA2Q2Rf5w0"
consumer_secret = "5tzcEpKRCXqkrgNuDllGRJ29lmRqW6lHjmvSuLXLiJH5RVg5Da"
access_key = "1440789160151826439-BFerR9hb6QX0RLDVl8rEBw9yp8fqst"
access_secret = "oAy9lXxrdILDlOETri8jHpOqlVSwN95eWM4eKRL5H7tcr"
    #authorize twitter, initialize tweepy


def imagedowload():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    alltweets = []
    tweets = api.user_timeline(id = "WHO", count = 10)
    alltweets.extend(tweets)
    oldestTweet = alltweets[-1].id - 1
    
    
    while len(tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        tweets = api.user_timeline("WHO",count=10,max_id=oldestTweet)
        
        #save most recent tweets
        alltweets.extend(tweets)
        
        #update the id of the oldest tweet less one
        oldestTweet = alltweets[-1].id - 1
        if(len(alltweets) > 100):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))
        
        ima = []

    for tweet in alltweets:
        media = tweet.entities.get('media', [])
        if(len(media) > 0):
            ima.append(media[0]['media_url'])

    index = 1
    for image in ima:
        print("image %s saved" %index)
        wget.download(image)
        print('\n')
        index += 1
    k = 1
    for twitter in alltweets:      
        print("Printing out the %s post id " %k)
        print(twitter.id)
        k+=1
 #write tweet objects to JSON
    file = open('testtest.json', 'w') 
    print ("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    print ("Done")
    file.close()

def dateandtime():
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    alltweets = []
    tweets = api.user_timeline(id = "KrisWu", count = 10)
    alltweets.extend(tweets)
    oldestTweet = alltweets[-1].id - 1
    
    
    while len(tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        tweets = api.user_timeline("KrisWu",count=10,max_id=oldestTweet)
        
        #save most recent tweets
        alltweets.extend(tweets)
        
        #update the id of the oldest tweet less one
        oldestTweet = alltweets[-1].id - 1
        if(len(alltweets) > 100):
            break
  
        dateandtime = []
        l = 1
    for tweets in alltweets:    
        print("The {0} post is originallly post at {1} ".format(l,tweets.created_at) )
        l += 1

def main():
    imagedowload()
    dateandtime()

if __name__ == '__main__':
    main()

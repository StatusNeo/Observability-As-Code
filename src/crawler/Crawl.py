''' Importing libraries '''
import tweepy
import csv
import pandas as pd

''' Authenticating Twitter Access with Developer Account '''
consumer_key = 'bIVfVMIgLtWaJAmrDqDEpRkwt'
consumer_secret = 'cTzQQCUyxHU7hDCMXaRtKTHeqTxEqA6lAaGaE5nbvrOF930VTY'
access_token = '1143353752792920065-S2JoUbphkswzmT5JP57WRalAaRR1mJ'
access_token_secret = 'I0EyYYGoJ5vDpu3gVY2foePUGuCSUf9pbofGP9J5TFZ1d'

''' Main Crawler Code'''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

''' Searching Tweets based on keyword'''
# Open/Create a file to append data
csvFile = open('info.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#StatusNeo",count=100,
                           lang="en",
                           since="2020-02-02").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

import tweepy
import os
from dotenv import load_dotenv
import time
from datetime import datetime

load_dotenv()

CONSUMER_KEY = os.getenv("API_KEY")
CONSUMER_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


while True:
    wanted_tweet = api.get_status(1357643189977505792)

    if (wanted_tweet.retweeted):
        api.unretweet(1357643189977505792)
        print("Unretweeted at : ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        time.sleep(7200)
    else:
        api.retweet(1357643189977505792)
        print("Retweeted at : ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        time.sleep(3600)



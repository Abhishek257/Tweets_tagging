import tweepy
3
consumer_key = "N4hwKMuDBtkqBiCq9EEeH5Ir4"
consumer_secret = "CmgycPzDczKzTPRwWgPNSiwSJC14H2baW05jr2iDaahswya1DF"
access_key = "3528419724-cn8MK1EXjKxxlimi3pzEMWJi6hhx3RdmpNZqQC3"
access_secret = "WeiARW5FEd6WCd6Bj0LAWAKNNpH9dAGdkKqjTYh7lqldd"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
fil=open("dirty_tweets.txt","w")
new_tweets = api.user_timeline(screen_name = "Modi",count=200)
for tweet in new_tweets[:5]:
    fil.writelines(tweet.text)

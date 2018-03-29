import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def hashtag(tweet):
    hashtags=re.findall(r"#(\w+)", tweet)
    print(hashtags)

def cleanr(tweet):
    cleaned_tweet=clean_tweet(tweet)
    cleaned_tweet=cleaned_tweet.lower()
    stop_words = list(set(stopwords.words('english')))
    word_tokens=word_tokenize(cleaned_tweet)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    print(filtered_sentence)

tweet="  you always show up at the right time. #istillbelieve!"
posfile=open("positive_tweets.txt",'r')
cleanr(tweet)
hashtag(tweet)

# for tweet in posfile:
#     clean(tweet)

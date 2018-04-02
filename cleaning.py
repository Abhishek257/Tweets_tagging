import re
import pickle
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
hashtags=[]
posunigram=[]
posbigram=[]
postrigram=[]
negunigram=[]
negbigram=[]
negtrigram=[]
count=0
def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def hashtag(tweet):
    hashtag=re.findall(r"#(\w+)", tweet)
    return hashtag

def cleanr(tweet):
    cleaned_tweet=clean_tweet(tweet)
    cleaned_tweet=cleaned_tweet.lower()
    stop_words = list(set(stopwords.words('english')))
    word_tokens=word_tokenize(cleaned_tweet)
    filtered_words = [w for w in word_tokens if not w in stop_words]
    return filtered_words


for line in open("positive_tweets.txt", encoding="utf-8").read().split("\n")[:-1]:
    i=0
    j=0
    pU = []
    pB = []
    pT = []
    hashtags.append(hashtag(line))
    pU=cleanr(line)
    posunigram = posunigram + pU
    while i < len(pU)-1:
        pB.append(pU[i] + pU[i+1])
        i += 1
    posbigram = posbigram + pB
    while j <  len(pU)-2:
        pT.append(pU[j] + pU[j+1] + pU[j+2])
        j += 1
    postrigram = postrigram + pT
    count += 1
    print(count)
most_common_posunigrams= [word for word, word_count in Counter(posunigram).most_common(3000)] #bigram
with open("most_common_posunigrams.pkl", "wb") as a1:
    pickle.dump(most_common_posunigrams, a1)
most_common_posbigrams= [word for word, word_count in Counter(posbigram).most_common(3000)] #bigram
with open("most_common_posbigrams.pkl", "wb") as a1:
    pickle.dump(most_common_posbigrams, a1)
most_common_postrigrams= [word for word, word_count in Counter(postrigram).most_common(3000)] #trigram
with open("most_common_postrigrams.pkl", "wb") as a1:
    pickle.dump(most_common_postrigrams, a1)
print("Most Common Positive Bigrams and Most Common positive Trigrams are Created.\n")

count=0
for line in open("negative_tweets.txt", encoding="utf-8").read().split("\n")[:-1]:
    i=0
    j=0
    nU = []
    nB = []
    nT = []
    hashtag(line)
    nU=cleanr(line)
    negunigram = negunigram + nU
    while i < len(nU)-1:
        nB.append(nU[i] + nU[i+1])
        i += 1
    negbigram = negbigram + nB
    while j <  len(nU)-2:
        pT.append(nU[j] + nU[j+1] + nU[j+2])
        j += 1
    negtrigram = negtrigram + nT
    count += 1
    print(count)
most_common_negunigrams= [word for word, word_count in Counter(negunigram).most_common(3000)] #bigram
with open("most_common_negunigrams.pkl", "wb") as a1:
    pickle.dump(most_common_negunigrams, a1)
most_common_negbigrams= [word for word, word_count in Counter(negbigram).most_common(3000)] #bigram
with open("most_common_negbigrams.pkl", "wb") as a1:
    pickle.dump(most_common_negbigrams, a1)
most_common_negtrigrams= [word for word, word_count in Counter(negtrigram).most_common(3000)] #trigram
with open("most_common_negtrigrams.pkl", "wb") as a1:
    pickle.dump(most_common_negtrigrams, a1)
print("Most Common negative Bigrams and Most Common negaitive Trigrams are Created.\n")
with open("hashtags.pkl", "wb") as a1:
    pickle.dump(hashtags, a1)

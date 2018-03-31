import pickle
from cleaning import hashtag,cleanr
from nltk.tokenize import word_tokenize
from numpy import array
from sklearn import svm,datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn import tree
univtrained = []
univnature = []
poslexicons = []
neglexicons = []
hashtags = []
posunigrams = []
negunigrams = []
negbigrams = []
posbigrams = []
postrigrams = []
negtrigrams = []
clf = svm.SVC()

#lexicons

for word in open("positivelexicon.txt", encoding="utf-8").read().split("\n")[:-1]:
    abc = word_tokenize(word)
    for a in abc:
        if a.isalnum():
            poslexicons.append(a)
for word in open("negativelexicon.txt", encoding="utf-8").read().split("\n")[:-1]:
    abc = word_tokenize(word)
    for a in abc:
        if a.isalnum():
            neglexicons.append(a)

#Unigrams

with (open("most_common_posunigrams.pkl", "rb")) as openfile:
    while True:
        try:
            posunigrams=(pickle.load(openfile))
        except EOFError:
            break
with (open("most_common_negunigrams.pkl", "rb")) as openfile:
    while True:
        try:
            negunigrams=(pickle.load(openfile))
        except EOFError:
            break

#bigrams

with (open("most_common_posbigrams.pkl", "rb")) as openfile:
    while True:
        try:
            posbigrams=(pickle.load(openfile))
        except EOFError:
            break
with (open("most_common_negbigrams.pkl", "rb")) as openfile:
    while True:
        try:
            negbigrams=(pickle.load(openfile))
        except EOFError:
            break

#trigrams

with (open("most_common_postrigrams.pkl", "rb")) as openfile:
    while True:
        try:
            postrigrams=(pickle.load(openfile))
        except EOFError:
            break
with (open("most_common_negtrigrams.pkl", "rb")) as openfile:
    while True:
        try:

            negtrigrams=(pickle.load(openfile))
        except EOFError:
            break

#hashtags

with (open("hashtags.pkl", "rb")) as openfile:
    while True:
        try:
            hashatags=(pickle.load(openfile))
        except EOFError:
            break

#Training positive

for line in open("positive_tweets.txt", encoding="utf-8").read().split("\n")[:-1]:
    i=0
    j=0
    abcd = []
    pU = []
    pB = []
    pT = []
    htag=[]
    unigram=[]
    bigram=[]
    trigram=[]
    htag=hashtag(line)
    pU=cleanr(line)
    unigram = unigram + pU
    while i < len(pU)-1:
        pB.append(pU[i] + pU[i+1])
        i += 1
    bigram = bigram + pB
    while j <  len(pU)-2:
        pT.append(pU[j] + pU[j+1] + pU[j+2])
        j += 1
    trigram = trigram + pT
    # feature  1
    positive=0
    negative=0
    for word in unigram:
        positive += posunigrams.count(word)
    for word in unigram:
        negative += negunigrams.count(word)
    if positive > negative:
        abcd.append(1)
    else:
        abcd.append(2)
     # feature  2
    positive=0
    negative=0
    for word in bigram:
        positive += posbigrams.count(word)
    for word in bigram:
        negative += negbigrams.count(word)
    if positive > negative:
        abcd.append(1)
    else:
        abcd.append(2)
    # feature 3
    positive = 0
    negative = 0
    for word in trigram:
        positive += postrigrams.count(word)
    for word in trigram:
        negative += negtrigrams.count(word)
    if positive > negative:
        abcd.append(1)
    else:
        abcd.append(2)
    # feature 4
    positive=0
    negative=0
    for word in unigram:
        positive += poslexicons.count(word)
    for word in unigram:
        negative += neglexicons.count(word)
    if positive > negative:
        abcd.append(positive)
    else:
        abcd.append(negative)
    # feature 5
    countr=0
    for word in hashtags:
        countr += htag.count(word)
    abcd.append(countr)
    univtrained.append(abcd)
    univnature.append(1)


#Training negative

for line in open("negative_tweets.txt", encoding="utf-8").read().split("\n")[:-1]:
    i=0
    j=0
    abcd = []
    pU = []
    pB = []
    pT = []
    htag=[]
    unigram=[]
    bigram=[]
    trigram=[]
    htag=hashtag(line)
    pU=cleanr(line)
    unigram = unigram + pU
    while i < len(pU)-1:
        pB.append(pU[i] + pU[i+1])
        i += 1
    bigram = bigram + pB
    while j <  len(pU)-2:
        pT.append(pU[j] + pU[j+1] + pU[j+2])
        j += 1
    trigram = trigram + pT
    # feature  1
    positive=0
    negative=0
    for word in unigram:
        positive += posunigrams.count(word)
    for word in unigram:
        negative += negunigrams.count(word)
    if positive > negative:
        abcd.append(1)
    else:
        abcd.append(2)
    # feature  2
    positive=0
    negative=0
    for word in bigram:
        positive += posbigrams.count(word)
    for word in bigram:
        negative += negbigrams.count(word)
    if positive > negative:
        abcd.append(1)
    else:
        abcd.append(2)
    # feature 3
    positive = 0
    negative = 0
    for word in trigram:
        positive += postrigrams.count(word)
    for word in trigram:
        negative += negtrigrams.count(word)
    if positive > negative:
        abcd.append(1)
    else:
        abcd.append(2)
    # feature 4
    positive = 0
    negative = 0
    for word in unigram:
        positive += poslexicons.count(word)
    for word in unigram:
        negative += neglexicons.count(word)
    if positive > negative:
        abcd.append(positive)
    else:
        abcd.append(negative)
    # feature 5
    countr=0
    for word in hashtags:
        countr += htag.count(word)
    abcd.append(countr)
    univtrained.append(abcd)
    univnature.append(0)


#Making feature list


univtrained=array(univtrained)
univnature=array(univnature)
clf.fit(univtrained, univnature)
with open("Trained_clf.pkl", "wb") as a:
    pickle.dump(clf, a)
iris=datasets.load_iris()
gnb=GaussianNB()
gnb.fit(univtrained,univnature)
with open("Trained_gnb.pkl","wb") as a:
    pickle.dump(gnb,a)
mnb=MultinomialNB().fit(univtrained, univnature)
with open("Trained_MultinomialNB.pkl","wb") as a:
    pickle.dump(mnb,a)
clf=BernoulliNB().fit(univtrained,univnature)
with open("Trained_bernoulli.pkl", "wb") as a:
    pickle.dump(clf, a)
DTclf = tree.DecisionTreeClassifier()
DTclf=DTclf.fit(univtrained,univnature)
with open("Trained_decisionTree.pkl", "wb") as a:
    pickle.dump(DTclf, a)
print("Training done....")

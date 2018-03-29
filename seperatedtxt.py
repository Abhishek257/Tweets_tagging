positivesent=open("positive_tweets1.txt","w")
negativesent=open("negative_tweets1.txt","w")
with open("Sentimental Analysis Dataset.csv", 'r') as csvfile:
    for row in csv.reader(csvfile):
        if(row[1] == '0'):
            print(negativesent.write(row[2]+"\n"))
        else:
            print(positivesent.write(row[2]+"\n"))

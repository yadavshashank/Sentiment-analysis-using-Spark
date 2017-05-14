# This program demonstrated the use of TextBlob library

from textblob import TextBlob
import re

File=open('StopWords.txt','r')
allLines=File.readlines()
File.close()

stopFile=[]
for i in allLines:
    stopFile.append(i.strip())

File2=open('processedNeutral.txt','r')
lines=File2.readlines()
File2.close()


#We are removing stop words , correcting spellings and converting all words to lowercase
count=0
wordList=[]
for i in lines:
    blob = TextBlob(i)
    text=list(set(((blob.correct()).lower()).words) - set(stopFile))
    for sub in text:
        wordList.append(sub)
        count=count+1
        print count,"\n"

print len(wordList),"\n"

File3=open('neutralTweetWords.txt','a')

for i in wordList:
    File3.write(i)
    File3.write(',')
File3.close()




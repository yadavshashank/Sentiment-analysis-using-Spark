# This program's function is to pre-process the tweet to remove impurities and replace slangs

import re
import slangDatabase



File=open('positiveTweets.txt','r')
allLines=File.readlines()
File.close()

lis=[]
slangDictionary=slangDatabase.transfer()
# Removing all hashtags, tags, http and all other impurities
for i in allLines:
    iter1=re.sub('@.*? ','', i)
    iter2=re.sub('#.*? ','',iter1)
    iter3=re.sub('http.*?\n','',iter2)
    iter4=re.sub('RT ','',iter3)
    iter5=re.sub('#.*?\n','',iter4)
    iter6=re.sub('@.*?\n','',iter5)
    iter7=iter6.decode('unicode_escape').encode('ascii','ignore')
    updatedIter7=iter7.replace('\n','')
    iter8="".join(updatedIter7)
    iter9=iter8.replace('&gt;','')
    iter10=iter9.replace('"','')
    iter11=iter10.replace('&amp;','')
    iter12=iter11.replace('&lt;','')

    lis.append(iter12)



lis2=[]
for i in lis:
    lis2.append(i.split())





# To replace all emoticons and slangs in the lines with their corresponding english word

def finalTweetFilter(lis,lis2,slangDictionary):
    finalTweet=[]
    for i in lis:
        flag=0
        lis2=i.split()
        string = []

        for j in lis2:
            if slangDictionary.has_key(j):

                string.append(j)
                flag=flag+1

        if flag==0:
            finalTweet.append(i)
        else:
            for j in string:
                # i = i.replace(j, slangDictionary[j])

                i = re.sub(re.escape(j),re.escape(slangDictionary[j]),i)

            finalTweet.append(i)
    return finalTweet


finalTweets=finalTweetFilter(lis,lis2,slangDictionary)
def transferTweet():
    return finalTweets

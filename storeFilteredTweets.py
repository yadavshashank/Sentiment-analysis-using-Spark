#This program will store filtered tweets into text finalTweets

import preProcessing
import re

tweets= preProcessing.transferTweet()
filteredTweet=[]

#Removing blank lines
for i in tweets:
    if re.match(r'^\s*$', i):
        continue
    else:
        filteredTweet.append(i)

File=open('processedPositive.txt','a')
for i in filteredTweet:
    save=i.replace("\\",'')
    File.write(save)
    File.write("\n")

File.close()

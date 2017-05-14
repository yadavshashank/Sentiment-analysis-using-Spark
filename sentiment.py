import sys
from pyspark import SparkConf,SparkContext
sc=SparkContext()

# Function to calculate the weight of each word under a category
def weights(x,limit):
	# read in text file and split each document into words
	tokenized = sc.textFile(x).flatMap(lambda line: line.split(","))
	Size=tokenized.count()
	# count the occurrence of each word
	wordCounts = tokenized.map(lambda word: (word, 1)).reduceByKey(lambda v1,v2:v1+v2)

	# filter out words with fewer than threshold occurrences
	filtered = wordCounts.filter(lambda pair:pair[1] >= limit)
	Prob=filtered.map(lambda (a,b):(a,float(b)/float(Size)))
	print ("\n\n\n\n\n\n\n")
	return Prob.collect()

# Function to calculate the sentiment
def sentiment(positiveProb, negativeProb, neutralProb):
	tokenized = sc.textFile('/home/shashank/spark-2.1.0/test.txt').flatMap(lambda line: line.split(" "))
	Size=tokenized.count()
	wordCount = tokenized.map(lambda word: (word, 1)).reduceByKey(lambda v1,v2:v1+v2)

	sentenceList=wordCount.collect()
	sentenceDic={}
	for i in range(len(sentenceList)):
		sentenceDic[sentenceList[i][0]]=sentenceList[i][1]
	print sentenceDic,"\n\n\n\n\n\n"
	sentimentValue=0.0



	for i in range(len(negativeProb)):
		if sentenceDic.has_key(negativeProb[i][0]):
			sentimentValue=sentimentValue-negativeProb[i][1]
			# print "\n\n\nNegative : ",negativeProb[i][1],sentimentValue

	for i in range(len(positiveProb)):
		if sentenceDic.has_key(positiveProb[i][0]):
			sentimentValue=sentimentValue+positiveProb[i][1]
			# print "\n\n\nPositive : ",positiveProb[i][1],sentimentValue

	print "\n\n\n\nSentiment Value : ",sentimentValue,"\n\n\n"

	if sentimentValue >= -0.00019 and sentimentValue <= 0.0001:
		print "\n\nNeutral Tweet\n\n\n\n"
	elif sentimentValue > 0.0001:
		print "\n\nPositive Tweet\n\n\n\n"
	else:
		print "\n\nNegative Tweet\n\n\n\n"





threshold = 1
positiveProb=weights('positiveTweetWords.txt',threshold)
negativeProb=weights('negativeTweetWords.txt',threshold)
neutralProb=weights('neutralTweetWords.txt',threshold)

sentiment(positiveProb,negativeProb,neutralProb)

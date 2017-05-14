The pre-processing of the tweets was done using pure Python with no integration with spark.
Calculation of the sentiment value was done using Spark. 

-------Spark---------------

The test tweet needs to be entered in tweet.txt
Run sentiment.py in Spark environment

-------Pre-processing in Python------

Files responsible for streaming and tweet collection:
negativeStreaming.py
positiveStreaming.py
neutral.py

slangDatabase.py creates a slang dictionary (courtesy-NoSlang.com)
preProcessing.py pre-processes the tweets
storeFilteredTweets.py is an intermediate file that needs to be run
textBlob.py removes stop words


Files feeded to Spark to calculate sentiment value:
negativeTweetWords.txt
positiveTweetWords.txt
neutralTweetWords.txt

Note:All files need to be run manually, to generate text files under diferent names

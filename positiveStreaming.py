from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time


ckey='aV2F1UqL6srKECq93eJusaT3O'
csecret='gh1XejimDQAZTFNf4SEDLTpM4LTWfUivuWA2BzrGotHi2NAyFQ'
atoken='2268407467-qpqvWGe58jEwfwgmDQ9pAh2wPrXHiLIGWXBhPER'
asecret='MO4PLtc9sbSNp1Gq4IINLgbVw3hiRr2RZ6hCi0rduxbKs'

class listener (StreamListener):
    def on_data(self, data):
        try:
            tweet = data.split(',"text":"')[1].split('","source')[0]

            save = tweet.split(',"source"')[0]
            saveThis =save.split('","display_text_range"')[0]
            # final = saveThis.split('","')[0]
            File= open('positiveTweets.txt','a')
            File.write(saveThis)
            File.write("\n")
            File.close()
            print data
            print "\n\n\n\n\n"
            return True
        except BaseException, e:
            print 'Failed on data,', str(e)
            time.sleep(5)

    def on_self(self, status):
        print status

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[":)",":-)",":')","=)",":]",":D",":-D","=D"],languages=["en"])

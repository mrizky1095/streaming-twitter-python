from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

# Authenticate
consumer_key = 'lJAVZF30ipVvo5Egd8efDlddh'
consumer_secret = 'IdqGaCKXZAdWBDI70pZqlH0xKkTvGC9Uhp4xqgMc8YILw2PMMW'

access_token = '150942159-sMWrknlZgxloS9k2GsJaMzXJfWGKXnulvZbZIkPT'
access_token_secret = 'MaVPLYlT7cfXCNiUBGM37bMTJbkiGmx6IYsIbUgH5KmjI'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # stream by user @myxl : 82552414
    # stream.filter(follow=['82552414'])

    # stream by keyword
    # stream.filter(track=['myxl', 'xl'])

    # stream by keyword & user
    stream.filter(follow=['82552414'], track=['myxl', 'xl'])

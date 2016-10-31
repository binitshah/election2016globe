from __future__ import print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
#import codecs

access_token = "2784350759-9bGnB5t1qyRJMFfWLhenzm7hZkInN8Qt9vFsKhL"
access_token_secret = "jGzhV5kLrLzqJNt9RkcLoREliF6FWnsbYns0WWVFd266B"
consumer_key = "zjwTbWUhkFUEbcSwWjgsP2Vi9"
consumer_secret = "r9uKy2qJsUwN0TU4W4auOMFqakzn4mObAMMnHtOoDoBf3ZKizV"

f = open('data.txt','w')

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        try:
            parsed_json = json.loads(data)
            if parsed_json['user']['location'] is not None:
                if "here" not in parsed_json['user']['location'] and "there" not in parsed_json['user']['location'] and "everywhere" not in parsed_json['user']['location'] and "in" not in parsed_json['user']['location'] and "your" not in parsed_json['user']['location']:
                    f.write(parsed_json['user']['location'] + '\n')
        except:
            pass

        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['clinton', 'trump', 'hillary', 'donald', 'pence', 'kaine'])
# credit to bence for the idea

import tweepy
import keys

class MyListener(tweepy.StreamListener):
    def __init__(self, username):
        super().__init__()
        user=username
        self.myStatus = False
        self.tweet = ''

    def on_status(self, status): 
        user=api.get_user(self.user)
        if status.user.id_str != user.id_str:
            return
        user = api.get_user(user)

        recipient_id = user
        text = 'good tweet!'
        dm = api.send_direct_message(user, text)

auth = tweepy.OAuthHandler(keys.ckey, keys.csecret)
auth.set_access_token(keys.atoken, keys.asecret)
api = tweepy.API(auth)

#must provide username here
user = api.get_user('jack')

listener = MyListener(user)

stream = tweepy.Stream(auth, listener)
stream.filter(follow=[user.id_str], is_async=True)
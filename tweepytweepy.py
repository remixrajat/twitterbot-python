import tweepy
import time

auth = tweepy.OAuthHandler('j54jZveGCVMzITIdLUxntsYGo', '5EGNjXWsmXer2OBzOcvwcx360qTWkV10utboY3Ox8wNqWQIzI7')
auth.set_access_token('1257377291249713152-hx2dbVqYkmpZO2QtZkq1v1tHydTfu7', 'wNwIPRgIAwi9oeZ24hZ9FubBZBTwAaDJQREvYFBNkMNry')

api = tweepy.API(auth)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


#Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)
    if follower.name == "Rajpal Singh Chauhan":
        follower.follow()
        break

# search_str = 'Party'
# number_of_tweets = 2
# for tweet in tweepy.Cursor(api.search, search_str).items(number_of_tweets):
#     try:
#         tweet.favorite()
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break
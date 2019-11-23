import os
import tweepy
from dotenv import load_dotenv, find_dotenv
from scripts import error_handler

# Load environment settings.
load_dotenv(find_dotenv())

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Set up API.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Fetch lists we've been added to.
lists = api.lists_memberships()

for entry in lists:
    try:
        creator_screen_name = entry.user.screen_name
        api.create_block(screen_name=creator_screen_name)
        print('Blocked @{}, creator of "{}".'.format(creator_screen_name, entry.name))
    except Exception as e:
        # Return human readable error message on fail
        error_handler(e.api_code)

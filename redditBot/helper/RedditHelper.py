import praw
from decouple import config


class RedditHelper(object):

    @staticmethod
    def getRedditConnection():
        return praw.Reddit(
            client_id=config('CLIENT_ID'),
            client_secret=config('CLIENT_SECRET'),
            user_agent=config('USER_AGENT')
        )
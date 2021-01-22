from time import sleep

from entity.LastStreamContainer import LastStreamContainer
from helper.RedditHelper import RedditHelper

from manager.comment.CommentManager import CommentManager


# Class containing the main logic of the bot.
class Bot(object):

    def __init__(self):
        # Initializing the connexion with reddit.
        self.reddit = RedditHelper.getRedditConnection()
        # Creating the object containing the bot information.
        self.latestStream = LastStreamContainer()
        # Initializing the comment manager, for handling chat suggestions.
        self.commentManager = CommentManager(self.latestStream)

    # Allows to start the bot and to initialise the reddit connexion
    def startBot(self):
        # Initializing the last stream found on Ari's reddit.
        self.getLatestStream()
        # Starting the bot loop.
        self._runBotLoop()

    # The loop that will be executed by the bot
    def _runBotLoop(self):
        counter = 0
        print('Starting the first loop')
        while 1 == 1:
            print("in loop")
            # Getting the latest stream.
            self.getLatestStream()
            # Getting the comments of the stream
            self.commentManager.readCommentFromLatestStream()
            # Waiting 10 seconds.
            print("loop end waiting for 10s")
            sleep(10)

    # Check if the stream is the latest.
    def getLatestStream(self):
        # Getting the post for Ari.
        lastPosts = self.reddit.redditor('arist0ttle').submissions.new(limit=2)
        i = -1
        # Iterating through the posts
        for lastPost in lastPosts:
            i += 1  # Skipping the first one since it's a stickied one
            if i == 0:
                continue
            # A new reddit thread has been detected.
            if self.latestStream.lastPostId is None or self.latestStream.lastPostId != lastPost.id:
                self.latestStream.lastPostId = lastPost.id
                self.latestStream.lastPost = lastPost

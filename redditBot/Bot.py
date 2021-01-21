import praw
from decouple import config

from BotContainer import BotContainer


# Allows to start the bot and to initialise the reddit connexion
def startBot():
    reddit = praw.Reddit(
        client_id=config('CLIENT_ID'),
        client_secret=config('CLIENT_SECRET'),
        user_agent=config('USER_AGENT')
    )
    # Getting the last stream to listen to.
    lastSavedPost = BotContainer()
    getLatestStream(reddit, lastSavedPost)
    # Getting the comments of the stream
    searchSuggestionsInComments(lastSavedPost)


# Check if the stream is the latest.
def getLatestStream(reddit, lastPostSaved):
    # Getting the post for Ari.
    lastPosts = reddit.redditor('arist0ttle').submissions.new(limit=2)
    i = -1
    # Iterating through the posts
    for lastPost in lastPosts:
        i += 1  # Skipping the first one since it's a stickied one
        if i == 0:
            continue
        # A new reddit thread has been detected.
        if lastPostSaved.lastPostId is None or lastPostSaved.lastPostId != lastPost.id:
            lastPostSaved.lastPostId = lastPost.id
            lastPostSaved.lastPost = lastPost


# Getting the new comments and parsing them.
def searchSuggestionsInComments(lastSavedPost):
    # Setting the sort order to newest comment first.
    lastSavedPost.lastPost.comment_sort = "new"
    # Getting the comment of the post.
    comments = lastSavedPost.lastPost.comments
    if len(comments) == 0:
        return
    # Checking if there is new comments.
    if comments[0].created_utc <= lastSavedPost.lastCommentProcessedTime:
        # No new comments, nothing to do.
        return
    # Extracting the comments
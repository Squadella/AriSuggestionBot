from Constants import BOT_INVOKE_STR
from string import punctuation


# Allows to extract a suggestion from the comment.
class CommentSuggestionExtractor(object):

    def __init__(self, latestStream):
        self.latestStream = latestStream
        # The array containing all the suggestion that will be extracted.
        self.suggestions = []

    # Extract the suggestion from a comment
    def extractSuggestionFromComments(self, comments):
        # If no new comment were detected we wait.
        if not self._hasNewComments(comments):
            return
        # Iterating through comments to find the bot tag
        for comment in comments:
            if self._isNewComment(comment):
                print('New comments found !')
                self._processComment(comment)
            else:
                # no new comment we end the loop.
                break
        # The setting the date of the last processed element
        self.latestStream.lastCommentTimeExtracted = comments[0].created_utc

    # Process a comment to extract a suggestion.
    def _processComment(self, comment):
        # Checks if the comment start with the bot call
        if not comment.body.lower().startswith(BOT_INVOKE_STR):
            return  # The comment isn't for the bot.
        # Extract the suggestion.
        suggestion = comment.body[len(BOT_INVOKE_STR):].strip(punctuation).strip()
        # Adding the suggestion
        self.suggestions.append(suggestion)

    # Check if the last time of the last analyzed comment is before the comment we are processing now.
    def _hasNewComments(self, comments):
        if self.latestStream.lastCommentTimeExtracted is None:
            return True
        return comments[0].created_utc > self.latestStream.lastCommentTimeExtracted

    def _isNewComment(self, comment):
        if self.latestStream.lastCommentTimeExtracted is None:
            return True
        return comment.created_utc > self.latestStream.lastCommentTimeExtracted

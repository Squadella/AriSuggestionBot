from manager.comment.extractor.CommentSuggestionExtractor import CommentSuggestionExtractor
from manager.comment.insert.SuggestionInsertManager import SuggestionInsertManager


class CommentManager(object):

    # Constructor
    # @param latestStream the latest stream found.
    def __init__(self, latestStream):
        self.latestStream = latestStream

    # Allows to read the comment from the latest stream found.
    def readCommentFromLatestStream(self):
        # Setting the sort order to newest comment first.
        self.latestStream.lastPost.comment_sort = "new"
        # Getting the comment of the post.
        comments = self.latestStream.lastPost.comments
        if len(comments) == 0:
            return
        extractor = CommentSuggestionExtractor(self.latestStream)
        # Trying to extract the comments from the thread.
        extractor.extractSuggestionFromComments(comments)
        SuggestionInsertManager.printSuggest(extractor.suggestions)


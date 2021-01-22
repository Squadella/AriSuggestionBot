# Object containing the information about the latest stream found.
class LastStreamContainer(object):

    def __init__(self):
        # The latest submission found on Ari's reddit profile
        self.lastPost = None
        # The latest submission id.
        self.lastPostId = None
        # The last time of the comment processed.
        self.lastCommentTimeExtracted = None

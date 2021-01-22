# Insert a list of suggestion into the database.
class SuggestionInsertManager(object):
    # Mettre une contrainte en base pour faire
    # planter les RQ qui insert 2x une suggestion pour un user

    @staticmethod
    def printSuggest(suggestions):
        for sug in suggestions:
            print(sug)

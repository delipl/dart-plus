
class Setting:
    def __init__(self, amountOfUsers=2, startPoints=301, doubleIn=False, doubleOut=False):
        self.amountOfUsers = amountOfUsers
        self.startPoints = startPoints
        self.doubleIn = doubleIn
        self.doubleOut = doubleOut

    def get_dictionary(self):
        return {
            "amountOfUsers": self.amountOfUsers,
            "startPoints": self.startPoints,
            "doubleIn": self.doubleIn,
            "doubleOut": self.doubleOut
        }

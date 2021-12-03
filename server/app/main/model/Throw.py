from datetime import datetime


class Throw:
    def __init__(self, multiplier, value):
        self.multiplier = multiplier
        self.value = value
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def getScore(self):
        return self.multiplier * self.value

    def get_dictionary(self):
        return {
            "multiplier": self.multiplier,
            "points": self.value,
            "date": self.date
        }

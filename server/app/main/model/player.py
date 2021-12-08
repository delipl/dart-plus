from app.main.model.throw import Throw
from app.main.util.config import get_dictionary


class Player:
    def __init__(self, id, nick, points, attempts):
        self.id = id
        self.nick = nick
        self.points = points
        self.attempts = attempts
        self.throws = []

    def addThrow(self, multiplier, value):
        self.throws.append(Throw(multiplier, value))

    def getLastThrow(self):
        if len(self.throws) == 0:
            return Throw(0, 0)
        else:
            return self.throws[-1]

    def get_dictionary(self):
        return {
            "id": self.id,
            "nick": self.nick,
            "points": self.points,
            "attempts": self.attempts,
            "throws": get_dictionary(self.throws)
        }

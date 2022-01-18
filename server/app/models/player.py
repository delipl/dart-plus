class Player:
    def __init__(self, user_id, points, nick):
        self.user_id = user_id
        self.points = points
        self.nick = nick
        self.attempts = 0
        self.throws_multiplier = 0
        self.throws_value = 0

    # def addThrow(self, multiplier, value):
    #     self.throws.append(Throw(multiplier, value))
    #
    # def getLastThrow(self):
    #     if len(self.throws) == 0:
    #         return Throw(0, 0)
    #     else:
    #         return self.throws[-1]
    #
    # def get_dictionary(self):
    #     return {
    #         "id": self.id,
    #         "nick": self.nick,
    #         "points": self.points,
    #         "attempts": self.attempts,
    #         "throws": get_dictionary(self.throws)
    #     }
    #
    # def to_json(self):
    #     json_post = {
    #         "id": self.id,
    #         "nick": self.nick,
    #         "points": self.points,
    #         "attempts": self.attempts,
    #         "throws": [self.throws_multiplier, self.throws_value]
    #     }
    #     return json_post

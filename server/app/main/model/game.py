from app.main.util.config import get_dictionary


class Game:
    def __init__(self, id, gameStatus, numberOfThrow, startTime, throwingUserId, round, setting, players=None):
        if players is None:
            players = []
        self.id = id
        self.gameStatus = gameStatus
        self.numberOfThrow = numberOfThrow
        self.startTime = startTime
        self.throwingUserId = throwingUserId
        self.round = round
        self.setting = setting
        self.players = players

    def get_dictionary(self):
        return {
            "id": self.id,
            "gameStatus": self.gameStatus,
            "numberOfThrow": self.numberOfThrow,
            "startTime": self.startTime,
            "throwingUserId": self.throwingUserId,
            "round": self.round,
            "setting": self.setting.get_dictionary(),
            "players": get_dictionary(self.players)
        }

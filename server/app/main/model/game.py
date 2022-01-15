import datetime
from app.main.util.config import get_dictionary
from app import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gameStatus = db.Column(db.Integer, index=True)
    numberOfThrow = db.Column(db.Integer, index=True)
    startTime = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    throwingUserId = db.Column(db.Integer, index=True)
    round = db.Column(db.Integer, index=True)

    #Relacje tu zrobic
    # self.setting = setting
    # self.players = players
    def __init__(self, id, gameStatus, numberOfThrow, startTime, throwingUserId, round, setting, players=None):
        if players is None:
            players = []

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

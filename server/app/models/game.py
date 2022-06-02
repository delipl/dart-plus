import datetime
from config import get_dictionary
from app import db


class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    gameStatus = db.Column(db.Integer)
    startTime = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    throwingUserId = db.Column(db.Integer, index=True)
    round = db.Column(db.Integer)
    # from setting
    startPoints = db.Column(db.Integer)
    doubleIn = db.Column(db.Boolean, default=False)
    doubleOut = db.Column(db.Boolean, default=False)
    # players is in user_game relationship
    # relationship with dartBoard
    boards = db.relationship('DartBoard', backref='game', lazy='dynamic')

    def to_json(self):
        players_id = [player.id for player in self.players]
        json_post = {
            "id": self.id,
            "gameStatus": self.gameStatus,
            "startTime": self.startTime.strftime("%m/%d/%Y, %H:%M:%S"),
            "throwingUserId": self.throwingUserId,
            "round": self.round,
            "startPoints": self.startPoints,
            "doubleIn": self.doubleIn,
            "doubleOut": self.doubleOut,
            "users_id": players_id
        }
        return json_post

    # def get_settings_to_json(self):
    #     players_id = [player.id for player in self.players]
    #     json_post = {
    #         "id": self.id,
    #         "startPoints": self.startPoints,
    #         "doubleIn": self.doubleIn,
    #         "doubleOut": self.doubleOut,
    #         "players": [player.player_to_json_setting() for player in self.players]
    #     }
    #     return json_post


    def get_settings_to_json(self):
        players_id = [player.id for player in self.players]
        json_post = {
            "id": self.id,
            "startPoints": self.startPoints,
            "doubleIn": self.doubleIn,
            "doubleOut": self.doubleOut,
            "players": [player.to_json() for player in self.players]
        }
        return json_post
import datetime
from config import get_dictionary
from app import db
from app.models.player import Player


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

    def to_json(self):
        players_id = [player.id for player in self.players]
        json_post = {
            "id": self.id,
            "gameStatus": self.gameStatus,
            "startTime": self.startTime,
            "throwingUserId": self.throwingUserId,
            "round": self.round,
            "startPoints": self.startPoints,
            "doubleIn": self.doubleIn,
            "doubleOut": self.doubleOut,
            "users_id": players_id
        }
        return json_post

# TODO value i multiplier muszą byc dodawane, jak nie tu, to w playerze w funkcji typu update_from_json
    def update_from_json(self, json_post):
        self.gameStatus = json_post.get('status')
        self.numberOfThrow = json_post.get('numberOfThrow')
        self.throwingUserId = json_post.get('throwingUserId')
        self.round = json_post.get('round')


        # multiplier = game_details["multiplier"]
        # value = game_details["value"]
        # playerList = game_details["playerList"]
        # TODO dodaj relacyjne argumenty [players] konstruktora game
        #setting_id = json_post.get('setting_id')

        return self

import datetime
from config import get_dictionary
from app import db


# Single game class that allows for many-to-many relationship with User

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    gameStatus = db.Column(db.Integer)
    numberOfThrow = db.Column(db.Integer)
    startTime = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    throwingUserId = db.Column(db.Integer, index=True)
    round = db.Column(db.Integer)

    # TODO Relacje ponizej mogą być źle, robione na szybko bez sprawdzenia
    setting_id = db.Column(db.Integer, db.ForeignKey('settings.id'))
    users_ids = db.relationship('User', backref='game', lazy='dynamic')
    players_ids = db.relationship('Player', backref='game', lazy='dynamic')

    def to_json(self):
        json_post = {
            "id": self.id,
            "gameStatus": self.gameStatus,
            "numberOfThrow": self.numberOfThrow,
            "startTime": self.startTime,
            "throwingUserId": self.throwingUserId,
            "round": self.round,
            "setting": self.setting.get_dictionary(),
            "players": get_dictionary(self.players)
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

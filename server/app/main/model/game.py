import datetime
from config import get_dictionary
from app import db


# Single game class that allows for many-to-many relationship with User
class Match(db.Model):
    __tablename__ = 'matches'
    users_ids = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), primary_key=True)


class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    gameStatus = db.Column(db.Integer)
    numberOfThrow = db.Column(db.Integer)
    startTime = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    throwingUserId = db.Column(db.Integer, index=True)
    round = db.Column(db.Integer)

    #Relacje tu zrobic
    setting_id = db.Column(db.Integer, db.ForeignKey('settings.id'))
    users_ids = db.relationship('Match', foreign_keys=[Match.users_ids],
                                backref=db.backref('user', lazy='joined'), lazy='dynamic',
                                cascade='all, delete-orphan')
    players_ids = db.relationship('Player', backref='game', lazy='dynamic')

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


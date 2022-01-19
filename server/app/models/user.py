import datetime

from app import db
from werkzeug.security import generate_password_hash, check_password_hash

user_game = db.Table('user_game',
                     db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                     db.Column('game_id', db.Integer, db.ForeignKey('games.id'))
                     )


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(128))
    name = db.Column(db.String(64), unique=True, index=True)
    nick = db.Column(db.String(64), unique=True, index=True)
    phone = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    throws = db.Column(db.Integer)

    # relacje z setting
    active_games = db.relationship('Game', secondary=user_game, backref='players')
    # player data
    attempts = db.Column(db.Integer)
    throws_multiplier = db.Column(db.Integer)
    throws_value = db.Column(db.Integer)
    points = db.Column(db.Integer)

    # @property
    # def password(self):
    #     raise AttributeError('Cannot read password attribute')
    #
    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)

    def to_json(self):
        games_ids = [game.id for game in self.active_games]
        json_post = {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "password": self.password,
            "nick": self.nick,
            "wins": self.wins,
            "throws": self.throws,
            "games_id": games_ids,
            "multiplier": self.throws_multiplier,
            "value": self.throws_value,
            "attempts": self.attempts
        }
        return json_post

    def player_to_json(self):
        json_post = {
            "id": self.id,
            "nick": self.nick,
            "points": self.points,
            "attempts": self.attempts,
            #TODO tu może być błąd, nie wiem jak wygląda throw w jsonie
            "throws": [self.throws_multiplier, self.throws_value]
        }
        return json_post

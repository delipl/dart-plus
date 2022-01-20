import datetime

from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from .. import login_manager


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
    phone = db.Column(db.Integer, unique=True)
    wins = db.Column(db.Integer)

    # member_since = db.Column(db.DateTime(), default=datetime.datetime.utcnow)


    # relacje z setting
    active_games = db.relationship('Game', secondary=user_game, backref='players')
    # relacja z throw
    throws = db.relationship('Throw', backref='player', lazy='dynamic')
    # player data
    attempts = db.Column(db.Integer)
    points = db.Column(db.Integer)

    # @property
    # def password(self):
    #     raise AttributeError('Cannot read password attribute')

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
            "throws": [throw.getScore() for throw in self.throws],
            "games_id": games_ids,
            "attempts": self.attempts,
        }
        return json_post

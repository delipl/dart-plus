import datetime
from config import get_dictionary
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean, default=False)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64), unique=True, index=True)
    nick = db.Column(db.String(64), unique=True, index=True)
    phone = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    throws = db.Column(db.Integer)
    #relacje
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))

    def get_dictionary(self):
        return {
            "id": self.id,
            "admin": self.admin,
            "password": self.password,
            "name": self.name,
            "nick": self.nick,
            "phone": self.phone,
            "wins": self.wins,
            "gamesId": self.gameIds,
            "throws": get_dictionary(self.throws)
        }

    @property
    def password(self):
        raise AttributeError('Cannot read password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


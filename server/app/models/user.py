import datetime

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
    # relacje
    setting_id = db.Column(db.Integer, db.ForeignKey('settings.id'))
    # player data
    points = db.Column(db.Integer)
    attempts = db.Column(db.Integer)
    throws_multiplier = db.Column(db.Integer, index=True)
    throws_value = db.Column(db.Integer, index=True)

    @property
    def password(self):
        raise AttributeError('Cannot read password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        json_post = {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
        }

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

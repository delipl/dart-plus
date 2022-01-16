from app.models.throw import Throw
from config import get_dictionary
from app import db


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(64))
    points = db.Column(db.Integer)
    attempts = db.Column(db.Integer)
    # TODO throw zapisywać w bazie danych jako pickle, poprawić funkcje dodawania rzutu itd
    throws_multiplier = db.Column(db.Integer, index=True)
    throws_value = db.Column(db.Integer, index=True)
    # Relationships
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    user_id = db.relationship('User', backref='player', lazy='dynamic')

    def addThrow(self, multiplier, value):
        self.throws.append(Throw(multiplier, value))

    def getLastThrow(self):
        if len(self.throws) == 0:
            return Throw(0, 0)
        else:
            return self.throws[-1]

    def get_dictionary(self):
        return {
            "id": self.id,
            "nick": self.nick,
            "points": self.points,
            "attempts": self.attempts,
            "throws": get_dictionary(self.throws)
        }

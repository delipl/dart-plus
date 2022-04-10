from datetime import datetime
from app import db


class Throw(db.Model):
    __tablename__ = 'throws'
    id = db.Column(db.Integer, primary_key=True)
    multiplier = db.Column(db.Integer)
    value = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def getScore(self):
        return self.multiplier * self.value


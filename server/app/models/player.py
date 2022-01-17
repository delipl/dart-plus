# from config import get_dictionary
# from app import db
# from app.models.throw import Throw
#
#
# class Player(db.Model):
#     __tablename__ = 'players'
#     id = db.Column(db.Integer, primary_key=True)
#     nick = db.Column(db.String(64))
#     points = db.Column(db.Integer)
#     attempts = db.Column(db.Integer)
#     throws_multiplier = db.Column(db.Integer, index=True)
#     throws_value = db.Column(db.Integer, index=True)
#     # Relationships
#     setting_id = db.Column(db.Integer, db.ForeignKey('settings.id'))
#     user = db.relationship('User', backref='player', lazy='dynamic')
#
#
#     def addThrow(self, multiplier, value):
#         self.throws.append(Throw(multiplier, value))
#
#     def getLastThrow(self):
#         if len(self.throws) == 0:
#             return Throw(0, 0)
#         else:
#             return self.throws[-1]
#
#     def get_dictionary(self):
#         return {
#             "id": self.id,
#             "nick": self.nick,
#             "points": self.points,
#             "attempts": self.attempts,
#             "throws": get_dictionary(self.throws)
#         }
#
#     def to_json(self):
#         json_post = {
#             "id": self.id,
#             "nick": self.nick,
#             "points": self.points,
#             "attempts": self.attempts,
#             "throws": [self.throws_multiplier, self.throws_value]
#         }
#         return json_post

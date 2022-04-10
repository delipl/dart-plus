from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import db
from app.models.user import User


class DartBoard(db.Model):
    __tablename__ = 'dartBoards'
    id = db.Column(db.Integer, primary_key=True)
    # relationship with user
    users = db.relationship('User', backref='board', lazy='dynamic')

    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))

    # JWT authorization
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return DartBoard.query.get(data['id'])


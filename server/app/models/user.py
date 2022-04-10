from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from .. import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


user_game = db.Table('user_game',
                     db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                     db.Column('game_id', db.Integer, db.ForeignKey('games.id'))
                     )


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64), unique=True, index=True)
    nick = db.Column(db.String(64), unique=True, index=True)
    phone = db.Column(db.Integer, unique=True)
    wins = db.Column(db.Integer)

    # relationship with setting
    active_games = db.relationship('Game', secondary=user_game, backref='players')
    # relationship with throw
    throws = db.relationship('Throw', backref='player', lazy='dynamic')
    # relationship with dartboard
    board_id = db.Column(db.Integer, db.ForeignKey('dartBoards.id'))
    # player data
    attempts = db.Column(db.Integer)
    points = db.Column(db.Integer)

    @property
    def password(self):
        raise AttributeError('Cannot read password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],
                       expires_in=expiration)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    def to_json(self):
        games_ids = [game.id for game in self.active_games]
        json_post = {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "password": self.password_hash,
            "nick": self.nick,
            "wins": self.wins,
            "throws": [throw.getScore() for throw in self.throws],
            "games_id": games_ids,
            "attempts": self.attempts,
        }
        return json_post

    def player_to_json_setting(self):
        json_post = {
            "id": self.id,
            "nick": self.nick,
            "board_id": self.board_id
        }
        return json_post

    def player_to_json_game_update(self):
        json_post = {
            "nick": self.nick,
            "points": self.points,
            'attempts': self.attempts
        }
        return json_post

    def player_to_json_game_loop(self):
        json_post = {
            "nick": self.nick,
            "points": self.points,
            'id': self.id,
            'board_id': self.board_id,
            'attempts': self.attempts
        }
        return json_post


class AnonymousUser(AnonymousUserMixin):
    pass


login_manager.anonymous_user = AnonymousUser


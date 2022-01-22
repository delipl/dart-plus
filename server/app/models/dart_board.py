from app import db


class DartBoard(db.Model):
    __tablename__ = 'dartBoards'
    id = db.Column(db.Integer, primary_key=True)
    # relationship with user
    users = db.relationship('User', backref='board', lazy='dynamic')


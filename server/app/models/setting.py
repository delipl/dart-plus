from app import db


# TODO settings musi miec dostep do players_ids, bo na podstawie tego musi zacząć się gra
class Setting(db.Model):
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True)
    amountOfUsers = db.Column(db.Integer)
    startPoints = db.Column(db.Integer)
    doubleIn = db.Column(db.Boolean, default=False)
    doubleOut = db.Column(db.Boolean, default=False)

    # Relacje
    game = db.relationship('Game', backref='setting', lazy='dynamic')
    users = db.relationship('User', backref='setting', lazy='dynamic')

    def get_dictionary(self):
        return {
            "amountOfUsers": self.amountOfUsers,
            "startPoints": self.startPoints,
            "doubleIn": self.doubleIn,
            "doubleOut": self.doubleOut
        }


from app import db


# TODO settings musi miec dostep do players_ids, bo na podstawie tego musi zacząć się gra
class Setting(db.Model):
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True)
    amountOfUsers = db.Column(db.Integer)
    startPoints = db.Column(db.Integer)
    doubleIn = db.Column(db.Boolean, default=False)
    doubleOut = db.Column(db.Boolean, default=False)
    game = db.relationship('Game', backref='setting', lazy='dynamic')

    def get_dictionary(self):
        return {
            "amountOfUsers": self.amountOfUsers,
            "startPoints": self.startPoints,
            "doubleIn": self.doubleIn,
            "doubleOut": self.doubleOut
        }

    @staticmethod
    def from_json(json_post):
        game_id = json_post.get('id')
        numberOfPlayers = json_post.get('numberOfPlayers')
        startPoints = json_post.get('startPoints')
        doubleIn = json_post.get('doubleIn')
        doubleOut = json_post.get('doubleOut')
        playersId = json_post.get('playersId')
        return Setting(numberOfPlayers=numberOfPlayers, startPoints=startPoints, doubleIn=doubleIn,
                       doubleOut=doubleOut, playersId=playersId, game_id=game_id)

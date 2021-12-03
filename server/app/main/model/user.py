from app.main.util.config import get_dictionary


class User:
    def __init__(self, id, admin, password, name, nick, phone, wins, gameIds, throws):
        self.id = id
        self.admin = admin
        self.password = password
        self.name = name
        self.nick = nick
        self.phone = phone
        self.wins = wins
        self.gameIds = gameIds
        self.throws = throws

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
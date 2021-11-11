import sqlite3

DATABASE_NAME = 'database.db'


class Setting:
    def __init__(self, id, gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round):
        self.id = id
        self.gameStatus = gameStatus
        self.maxThrow = maxThrow
        self.numberOfThrow = numberOfThrow
        self.startTime = startTime
        self.throwingPlayerId = throwingPlayerId
        self.round = round

    def getDictionary(self):
        return {
            "id": self.id,
            "gameStatus": self.gameStatus,
            "maxThrow": self.maxThrow,
            "numberOfThrow": self.numberOfThrow,
            "startTime": self.startTime,
            "throwingPlayerId": self.throwingPlayerId,
            "round": self.round
        }


class Player:
    def __init__(self, id, name, nick, maxThrow, throws, average, wins, matches):
        self.id = id
        self.name = name
        self.nick = nick
        self.maxThrow = maxThrow
        self.throws = throws
        self.average = average
        self.wins = wins
        self.matches = matches

    def getDictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "nick": self.nick,
            "maxThrow": self.maxThrow,
            "throws": self.throws,
            "average": self.average,
            "wins": self.wins,
            "matches": self.matches,
        }


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS settings(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gameStatus BOOLEAN NOT NULL,
                maxThrow INTEGER NOT NULL,
                numberOfThrow INTEGER NOT NULL,
                startTime TEXT NOT NULL,
                throwingPlayerId INTEGER NOT NULL,
                round INTEGER NOT NULL
            )
            """,
            """CREATE TABLE IF NOT EXISTS players(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                nick TEXT NOT NULL,
                maxThrow INTEGER NOT NULL,
                throws INTEGER NOT NULL,
                average FLOAT NOT NULL,
                wins INTEGER NOT NULL,
                matches INTEGER NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

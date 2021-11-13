import sqlite3
from datetime import datetime

DATABASE_NAME = 'database.db'


class Settings:
    def __init__(self, amountOfUsers=2, startPoints=301, doubleIn=False, doubleOut=False):
        self.amountOfUsers = amountOfUsers
        self.startPoints = startPoints
        self.doubleIn = doubleIn
        self.doubleOut = doubleOut
        self.playersId = []

    def getDictionary(self):
        return {
            "amountOfUsers": self.amountOfUsers,
            "startPoints": self.startPoints,
            "doubleIn": self.doubleIn,
            "doubleOut": self.doubleOut
        }


class Game:
    def __init__(self, id, gameStatus, numberOfThrow, startTime, throwingUserId, round, setting, players = []):
        self.id = id
        self.gameStatus = gameStatus
        self.numberOfThrow = numberOfThrow
        self.startTime = startTime
        self.throwingUserId = throwingUserId
        self.round = round
        self.setting = setting
        self.players = players

    def getDictionary(self):
        return {
            "id": self.id,
            "gameStatus": self.gameStatus,
            "numberOfThrow": self.numberOfThrow,
            "startTime": self.startTime,
            "throwingUserId": self.throwingUserId,
            "round": self.round,
            "setting": self.setting.getDictionary(),
            "players": getDictionary(self.players)
        }


class User:
    def __init__(self, id, name, nick, phone, maxThrow, throws, average, wins, matches):
        self.id = id
        self.name = name
        self.nick = nick
        self.phone = phone
        self.maxThrow = maxThrow
        self.throws = throws
        self.average = average
        self.wins = wins
        self.matches = matches
        self.throws = []

    def getDictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "nick": self.nick,
            "phone": self.phone,
            "maxThrow": self.maxThrow,
            "throws": self.throws,
            "average": self.average,
            "wins": self.wins,
            "matches": self.matches,
            "throws": getDictionary(self.throws)
        }


class Player:
    def __init__(self, id, nick, points, attempts):
        self.id = id
        self.nick = nick
        self.points = points
        self.attempts = attempts
        self.throws = []

    def addThrow(self, multiplier, value):
        self.throws.append(Throw(multiplier, value))

    def getDictionary(self):
        return {
            "id": self.id,
            "nick": self.nick,
            "points": self.points,
            "attempts": self.attempts,
            "throws": getDictionary(self.throws)
        }


def getDictionary(objects: list):
    dict = []
    for i in objects:
        dict.append(i.getDictionary())
    return dict


class Throw:
    def __init__(self, multiplier, value):
        self.multiplier = multiplier
        self.value = value
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def getScore(self):
        return self.multiplier * self.value

    def getDictionary(self):
        return {
            "multiplier": self.multiplier,
            "points": self.value,
            "date": self.date
        }


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = []
    tables.append(
                """CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                nick TEXT NOT NULL,
                phone INTEGER NOT NULL,
                maxThrow INTEGER NOT NULL,
                throws INTEGER NOT NULL,
                average FLOAT NOT NULL,
                wins INTEGER NOT NULL,
                matches INTEGER NOT NULL
            )
            """)
    tables.append(
                """CREATE TABLE IF NOT EXISTS games(
                id INTEGER PRIMARY KEY,
                gameStatus INTEGER NOT NULL,
                numberOfThrow INTEGER NOT NULL,
                startTime TEXT NOT NULL,
                throwingUserId INTEGER NOT NULL,
                round INTEGER NOT NULL,
                setting pickle NOT NULL,
                players pickle NOT NULL
            )
            """)
    db = get_db()
    cursor = db.cursor()
    # dropTableStatement = "DROP TABLE games"
    # cursor.execute(dropTableStatement)
    for table in tables:
        cursor.execute(table)

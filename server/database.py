import random
import sqlite3
from datetime import datetime
import controller
from errors import *

DATABASE_NAME = 'database.db'
ID_MAX = 65535
ID_MIN = 50


class Settings:
    def __init__(self, amountOfUsers=2, startPoints=301, doubleIn=False, doubleOut=False):
        self.amountOfUsers = amountOfUsers
        self.startPoints = startPoints
        self.doubleIn = doubleIn
        self.doubleOut = doubleOut
        self.playersId = []

    def get_dictionary(self):
        return {
            "amountOfUsers": self.amountOfUsers,
            "startPoints": self.startPoints,
            "doubleIn": self.doubleIn,
            "doubleOut": self.doubleOut
        }


class Game:
    def __init__(self, id, gameStatus, numberOfThrow, startTime, throwingUserId, round, setting, players=None):
        if players is None:
            players = []
        self.id = id
        self.gameStatus = gameStatus
        self.numberOfThrow = numberOfThrow
        self.startTime = startTime
        self.throwingUserId = throwingUserId
        self.round = round
        self.setting = setting
        self.players = players

    def get_dictionary(self):
        return {
            "id": self.id,
            "gameStatus": self.gameStatus,
            "numberOfThrow": self.numberOfThrow,
            "startTime": self.startTime,
            "throwingUserId": self.throwingUserId,
            "round": self.round,
            "setting": self.setting.get_dictionary(),
            "players": get_dictionary(self.players)
        }


class User:
    def __init__(self, id, password, name, nick, phone, maxThrow, throws, average, wins, gameIds):
        self.id = id
        self.password = password
        self.name = name
        self.nick = nick
        self.phone = phone
        self.maxThrow = maxThrow
        self.throws = throws
        self.average = average
        self.wins = wins
        self.gameIds = gameIds
        self.throws = []

    def get_dictionary(self):
        return {
            "id": self.id,
            "password": self.password,
            "name": self.name,
            "nick": self.nick,
            "phone": self.phone,
            "maxThrow": self.maxThrow,
            "average": self.average,
            "wins": self.wins,
            "gamesId": self.gameIds,
            "throws": get_dictionary(self.throws)
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

    def getLastThrow(self):
        if len(self.throws) == 0:
            return Throw(0, 0)
        else:
            return self.throws[-1]

    def get_dictionary(self):
        return {
            "id": self.id,
            "nick": self.nick,
            "points": self.points,
            "attempts": self.attempts,
            "throws": get_dictionary(self.throws)
        }


class Throw:
    def __init__(self, multiplier, value):
        self.multiplier = multiplier
        self.value = value
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def getScore(self):
        return self.multiplier * self.value

    def get_dictionary(self):
        return {
            "multiplier": self.multiplier,
            "points": self.value,
            "date": self.date
        }


def generate_id():
    id = random.randint(ID_MIN, ID_MAX)
    while controller.get_user(id) != ERROR_USER_NOT_EXIST:
        id = random.randint(ID_MIN, ID_MAX)
    return id


def get_dictionary(objects: list):
    dictionary = []
    for i in objects:
        dictionary.append(i.get_dictionary())
    return dictionary


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = ["""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                password TEXT NOT NULL,
                name TEXT NOT NULL,
                nick TEXT NOT NULL,
                phone INTEGER NOT NULL,
                maxThrow INTEGER NOT NULL,
                throws INTEGER NOT NULL,
                average FLOAT NOT NULL,
                wins INTEGER NOT NULL,
                gameIds INTEGER NOT NULL
            )
            """, """CREATE TABLE IF NOT EXISTS games(
                id INTEGER PRIMARY KEY,
                gameStatus INTEGER NOT NULL,
                numberOfThrow INTEGER NOT NULL,
                startTime TEXT NOT NULL,
                throwingUserId INTEGER NOT NULL,
                round INTEGER NOT NULL,
                setting pickle NOT NULL,
                players pickle NOT NULL
            )
            """]
    db = get_db()
    cursor = db.cursor()
    # dropTableStatement = "DROP TABLE users"
    # cursor.execute(dropTableStatement)
    for table in tables:
        cursor.execute(table)

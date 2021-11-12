import sqlite3
from datetime import datetime

DATABASE_NAME = 'database.db'


class Settings:
    def __init__(self, amountOfUsers=2, startPoints=301, doubleIn=False, doubleOut=False):
        self.amountOfUsers = amountOfUsers
        self.startPoints = startPoints
        self.doubleIn = doubleIn
        self.doubleOut = doubleOut

    def getDictionary(self):
        return {
            "amountOfUsers": self.amountOfUsers,
            "startPoints": self.startPoints,
            "doubleIn": self.doubleIn,
            "doubleOut": self.doubleOut
        }


class Game:
    def __init__(self, id, gameStatus, maxThrow, numberOfThrow, startTime, throwingUserId, round, setting, players: list):
        self.id = id
        self.gameStatus = gameStatus
        self.maxThrow = maxThrow
        self.numberOfThrow = numberOfThrow
        self.startTime = startTime
        self.throwingUserId = throwingUserId
        self.round = round
        self.setting = setting
        self.players = []
        for p in range(setting.amountOfUsers - 1):
            self.players.append(Player(p, "Test" + str(p), setting.startPoints))

        # test throw
        pTest = Player(setting.amountOfUsers - 1, "TestThrow", setting.startPoints)
        pTest.addThrow(3, 20)
        pTest.addThrow(1, 17)
        pTest.addThrow(3, 2)
        pTest.calculateAverage() # test
        self.players.append(pTest)

    def getDictionary(self):
        return {
            "id": self.id,
            "gameStatus": self.gameStatus,
            "maxThrow": self.maxThrow,
            "numberOfThrow": self.numberOfThrow,
            "startTime": self.startTime,
            "throwingUserId": self.throwingUserId,
            "round": self.round,
            "setting": self.setting.getDictionary(),
            "players": getDictionary(self.players)
        }


class User:
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


class Player:
    def __init__(self, id, nick, points):
        self.id = id
        self.nick = nick
        self.points = points
        self.throws = []

    # test
    def calculateAverage(self):
        sum = 0
        for i in self.throws:
            sum = sum + i.multiplier * i.points
        print("Player " + str(self.id) + " average: " + str(round(sum / len(self.throws), 2)))

    def addThrow(self, multiplier, points):
        self.points = self.points - multiplier*points
        self.throws.append(Throw(multiplier, points))

    def removeLastThrow(self):
        self.removeThrow(len(self.throws)-1)

    def removeThrow(self, i):
        self.points = self.points + self.throws[i].multiplier * self.throws[i].points
        self.throws[i].remove(i)

    def getDictionary(self):
        return {
            "id": self.id,
            "nick": self.nick,
            "points": self.points,
            "throws": getDictionary(self.throws)
        }


def getDictionary(objects: list):
    dict = []
    for i in objects:
        dict.append(i.getDictionary())
    return dict


class Throw:
    def __init__(self, multiplier, points):
        self.multiplier = multiplier
        self.points = points
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def getScore(self):
        return self.multiplier * self.points

    def getDictionary(self):
        return {
            "multiplier": self.multiplier,
            "points": self.points,
            "date": self.date
        }


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS games(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gameStatus BOOLEAN NOT NULL,
                maxThrow INTEGER NOT NULL,
                numberOfThrow INTEGER NOT NULL,
                startTime TEXT NOT NULL,
                throwingUserId INTEGER NOT NULL,
                round INTEGER NOT NULL,
                setting pickle NOT NULL,
                players pickle NOT NULL
            )
            """,
        """CREATE TABLE IF NOT EXISTS users(
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

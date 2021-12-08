import pickle

from app.main.database.database import get_db
from app.main.model.game import Game


def insert_game(id, gameStatus, numberOfThrow, startTime, throwingUserId, round, setting, players):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO games(id, gameStatus, numberOfThrow, startTime, " \
                "throwingUserId, round, setting, players) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [id, gameStatus, numberOfThrow, startTime, throwingUserId, round, pickle.dumps(setting),
                               pickle.dumps(players)])
    db.commit()
    return True


def get_game(id):
    game = None
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM games WHERE id = ?"
    cursor.execute(query, [id])
    rows = cursor.fetchall()
    if len(rows) == 0:
        return "Game does not exist!"
    for i in rows:
        game = Game(i[0], i[1], i[2], i[3], i[4], i[5], pickle.loads(i[6]), pickle.loads(i[7]))
    return game


def get_games():
    games = []
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM games"
    cursor.execute(query)
    rows = cursor.fetchall()
    for i in rows:
        game = Game(i[0], i[1], i[2], i[3], i[4], i[5], pickle.loads(i[6]), pickle.loads(i[7]))
        games.append(game.get_dictionary())
    return games


def update_game(id, status, throwingPlayerId, multiplier, value, round, playerList):
    db = get_db()
    cursor = db.cursor()
    players = get_game(id).players

    for p in players:
        for i in range(len(playerList)):
            if p.id == playerList[i]["id"]:
                p.attempts = playerList[i]["attempts"]
                p.points = playerList[i]["points"]
                if 0 <= p.attempts < 3:
                    p.addThrow(multiplier, value)


    statement = "UPDATE games SET gameStatus = ?, throwingUserId = ?, round = ?, players = ? WHERE id = ?"
    cursor.execute(statement, [status, throwingPlayerId, round, pickle.dumps(players), id])
    db.commit()
    return True


def delete_game(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def delete_games():
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM games"
    cursor.execute(statement)
    db.commit()
    return True

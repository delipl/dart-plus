import pickle
from errors import *
from database import get_db, Game, User


def get_info(id):
    game = None
    db = get_db()
    cursor = db.cursor()
    query = 'SELECT * FROM games WHERE id = ?'
    cursor.execute(query, [id])
    rows = cursor.fetchall()
    if len(rows) == 0:
        return ERROR_GAME_NOT_EXIST
    for i in rows:
        game = Game(i[0], i[1], i[2], i[3], i[4], i[5], pickle.loads(i[6]), pickle.loads(i[7]))
    player = None
    players = []
    main_dictionary = {}
    for p in game.players:
        if p.attempts > 0:
            player = p
            break
    if player is None:
        player = game.players[0]
    game.players.remove(player)
    for p in game.players:
        dictionary = {"nick": p.nick, "points": p.points}
        players.append(dictionary)

    main_dictionary["nick"] = player.nick
    main_dictionary["points"] = player.points
    main_dictionary["attempts"] = 2
    main_dictionary["lastThrow"] = player.getLastThrow().getScore()
    main_dictionary["players"] = players
    return main_dictionary


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
        return ERROR_GAME_NOT_EXIST
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
                if 0 < p.attempts < 3:
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


def insert_user(id, password, name, nick, phone, maxThrow, throws, average, wins, gameIds):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO users(id, password, name, nick, phone, maxThrow, " \
                "throws, average, wins, gameIds) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [id, password, name, nick, phone, maxThrow,
                               pickle.dumps(throws), average, wins, pickle.dumps(gameIds)])
    db.commit()
    return True


def get_user(id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, [id])
    rows = cursor.fetchall()[0]
    if len(rows) == 0:
        return ERROR_USER_NOT_EXIST
    user = User(rows[0], rows[1], rows[2], rows[3], rows[4],
                rows[5], pickle.loads(rows[6]), rows[7], rows[8], pickle.loads(rows[9]))
    return user


def get_users():
    users = []
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    rows = cursor.fetchall()
    for i in rows:
        user = User(i[0], i[1], i[2], i[3], i[4],
                    i[5], pickle.loads(i[6]), i[7], i[8], pickle.loads(i[9]))
        users.append(user.get_dictionary())
    return users


def update_user(id, nick, password):
    db = get_db()
    cursor = db.cursor()
    user = get_user(id)
    if user == ERROR_USER_NOT_EXIST:
        return ERROR_USER_NOT_EXIST
    if password is None:
        password = user.password
    if nick is None:
        nick = user.nick
    statement = "UPDATE users SET nick = ?, password = ? WHERE id = ?"
    cursor.execute(statement, [nick, password, id])
    db.commit()
    return True


def delete_user(id):
    if get_user(id) == ERROR_USER_NOT_EXIST:
        return ERROR_USER_NOT_EXIST
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM users WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def delete_users():
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM users"
    cursor.execute(statement)
    db.commit()
    return True

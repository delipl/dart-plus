import pickle

from database import get_db, Game, User, Player, getDictionary
import pickle as p


def insert_games(id, gameStatus, numberOfThrow, startTime, throwingUserId, round, setting, players):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO games(id, gameStatus, numberOfThrow, startTime, " \
                "throwingUserId, round, setting, players) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [id, gameStatus, numberOfThrow, startTime, throwingUserId, round, p.dumps(setting),
                               p.dumps(players)])
    db.commit()
    return True


def insert_user(name, nick, maxThrow, throws, average, wins, matches):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO users(name, nick, maxThrow, throws, average, wins, matches) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [name, nick, maxThrow, throws, average, wins, matches])
    db.commit()
    return True


def get_games():
    games = []
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM games"
    cursor.execute(query)
    rows = cursor.fetchall()
    for i in rows:
        game = Game(i[0], i[1], i[2], i[3], i[4], i[5], pickle.loads(i[6]), pickle.loads(i[7]))
        games.append(game.getDictionary())
    return games


def get_info(id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM games WHERE id = ?"
    cursor.execute(query, [id])
    rows = cursor.fetchall()
    if len(rows) == 0:
        return "Game does not exist!"
    for i in rows:
        game = Game(i[0], i[1], i[2], i[3], i[4], i[5], pickle.loads(i[6]), pickle.loads(i[7]))
    player = None
    players = []
    dictionary = {}
    for p in game.players:
        if p.attempts > 0:
            player = p
            break
    if player == None:
        player = game.players[0]
    game.players.remove(player)  # nie wiem czy zadziala xd
    for p in game.players:
        dict = {}
        dict["nick"] = p.nick
        dict["points"] = p.points
        players.append(dict)

    dictionary["nick"] = player.nick
    dictionary["points"] = player.points
    dictionary["attempts"] = 2
    dictionary["lastThrow"] = player.throw.getScore()
    dictionary["players"] = players
    return dictionary


def get_gameDictionary(id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM games WHERE id = ?"
    cursor.execute(query, [id])
    rows = cursor.fetchall()
    if len(rows) == 0:
        return "Game does not exist!"
    for i in rows:
        game = Game(i[0], i[1], i[2], i[3], i[4], i[5], pickle.loads(i[6]), pickle.loads(i[7]))
    return game.getDictionary()


def get_game(id):
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


def get_user(id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, [id])
    rows = cursor.fetchall()
    if len(rows) == 0:
        return "User does not exist!"
    user = User(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7])
    return user.getDictionary()


def get_users():
    users = []
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    rows = cursor.fetchall()
    for i in rows:
        user = User(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        users.append(user.getDictionary())
    return users


def update_games(id, status, throwingPlayerId, multiplier, value, round, playerList):
    db = get_db()
    cursor = db.cursor()
    players = get_game(id).players
    for p in players:
        for i in range(len(playerList)):
            if p.id == i["id"]:
                p.attempts = i["attempts"]
                p.points = i["points"]

    print(players)
    statement = "UPDATE games SET gameStatus = ?, numberOfThrow = ?, " \
                "throwingUserId = ?, round = ?, setting = ?, players = ? WHERE id = ?"
    cursor.execute(statement, [status, throwingPlayerId, multiplier, value, round, players])
    db.commit()
    return True


def update_users(id, name, nick, maxThrow, throws, average, wins, matches):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE users SET name = ?, nick = ?, maxThrow = ?, " \
                "throws = ?, average = ?, wins = ?, matches = ? WHERE id = ?"
    cursor.execute(statement, [name, nick, maxThrow, throws, average, wins, matches, id])
    db.commit()
    return True


def delete_game(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM games WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def delete_user(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM users WHERE id = ?"
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


def delete_users():
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM users"
    cursor.execute(statement)
    db.commit()
    return True

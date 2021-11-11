from database import get_db, Setting, Player


# Insert settings table, that was happend when game has been started.
def insert_settings(gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO settings(gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round])
    db.commit()
    return True


# Insert player
def insert_player(name, nick, maxThrow, throws, average, wins, matches):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO players(name, nick, maxThrow, throws, average, wins, matches) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [name, nick, maxThrow, throws, average, wins, matches])
    db.commit()
    return True


# Get all settings
def get_settings():
    settings = []
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM settings"
    cursor.execute(query)
    rows = cursor.fetchall()
    for i in rows:
        setting = Setting(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        settings.append(setting.getDictionary())
    return settings


# Get all players
def get_players():
    players = []
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM players"
    cursor.execute(query)
    rows = cursor.fetchall()
    for i in rows:
        player = Player(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
        players.append(player.getDictionary())
    return players


# Update settings values
def update_settings(id, gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE settings SET gameStatus = ?, maxThrow = ?, numberOfThrow = ?, " \
                "startTime = ?, throwingPlayerId = ?, round = ? WHERE id = ?"
    cursor.execute(statement, [gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round, id])
    db.commit()
    return True


# Update players values
def update_players(id, name, nick, maxThrow, throws, average, wins, matches):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE players SET name = ?, nick = ?, maxThrow = ?, " \
                "throws = ?, average = ?, wins = ?, matches = ? WHERE id = ?"
    cursor.execute(statement, [name, nick, maxThrow, throws, average, wins, matches, id])
    db.commit()
    return True


# Delete setting from database
def delete_setting(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM settings WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


# Delete player from database
def delete_player(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM players WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


# Delete all setting
def delete_settings():
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM settings"
    cursor.execute(statement)
    db.commit()
    return True


# Delete all players
def delete_players():
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM players"
    cursor.execute(statement)
    db.commit()
    return True

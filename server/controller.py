from database import get_db


# Insert settings table, that was happend when game has been started.
def insert_settings(gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO settings(gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round])
    db.commit()
    return True


# Get all settings
def get_settings():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round FROM settings"
    cursor.execute(query)
    return cursor.fetchall()


# Update settings values
def update_game(gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round):
    id = 1 # at this moment we need one game
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE settings SET gameStatus = ?, maxThrow = ?, numberOfThrow = ?, " \
                "startTime = ?, throwingPlayerId = ?, round = ? WHERE id = ?"
    cursor.execute(statement, [gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round])
    db.commit()
    return True

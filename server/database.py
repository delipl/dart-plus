import sqlite3

DATABASE_NAME = 'database.db'


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
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

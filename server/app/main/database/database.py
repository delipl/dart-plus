import sqlite3
from app.main.util.config import DATABASE_NAME


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = ["""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                admin BOOLEAN NOT NULL,
                password TEXT NOT NULL,
                name TEXT NOT NULL,
                nick TEXT NOT NULL,
                phone INTEGER NOT NULL,
                wins INTEGER NOT NULL,
                gameIds INTEGER NOT NULL,
                throws pickle
            )
            """, """CREATE TABLE IF NOT EXISTS games(
                id INTEGER PRIMARY KEY,
                gameStatus INTEGER NOT NULL,
                numberOfThrow INTEGER NOT NULL,
                startTime TEXT NOT NULL,
                throwingUserId INTEGER NOT NULL,
                round INTEGER NOT NULL,
                setting pickle,
                players pickle
            )
            """]
    db = get_db()
    cursor = db.cursor()
    # dropTableStatement = "DROP TABLE games"
    # cursor.execute(dropTableStatement)
    for table in tables:
        cursor.execute(table)

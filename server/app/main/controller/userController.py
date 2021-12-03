import pickle

from app.main.database.database import get_db
from app.main.model.user import User
from app.main.util.config import ERROR_USER_NOT_EXIST


def insert_user(id, password, name, nick, phone, maxThrow, throws, average, wins, gameIds):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO users(id, password, name, nick, phone, maxThrow, " \
                "throws, average, wins, gameIds) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [id, password, name, nick, phone, maxThrow,
                               pickle.dumps(throws), average, wins, pickle.dumps(gameIds)])
    db.commit()
    dictionary = {"message": "Good"}
    return dictionary


def get_user(id):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, [id])
    rows = cursor.fetchall()
    if len(rows) == 0:
        return ERROR_USER_NOT_EXIST
    user = User(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4],
                rows[0][5], pickle.loads(rows[0][6]), rows[0][7])
    return user


def get_user_phone(phone):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE phone = ?"
    cursor.execute(query, [phone])
    rows = cursor.fetchall()
    if len(rows) == 0:
        return ERROR_USER_NOT_EXIST
    user = User(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4],
                rows[0][5], pickle.loads(rows[0][6]), rows[0][7])
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
                    i[5], pickle.loads(i[6]), i[7])
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

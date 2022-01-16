import pickle

from app.models.user import User


def insert_user(id, admin, password, name, nick, phone, wins, gameIds, throws):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO users(id, admin, password, name, " \
                "nick, phone, wins, gameIds, throws) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(statement, [id, admin, password, name, nick, phone, wins, pickle.dumps(gameIds), pickle.dumps(throws)])
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
        return "User does not exist!"
    user = User(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4],
                rows[0][5], rows[0][6], pickle.loads(rows[0][7]), pickle.loads(rows[0][8]))
    return user


def get_user_by_phone(phone):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE phone = ?"
    cursor.execute(query, [phone])
    rows = cursor.fetchall()
    if len(rows) == 0:
        return "User does not exist!"
    user = User(rows[0][0], rows[0][1], rows[0][2], rows[0][3], rows[0][4],
                rows[0][5], rows[0][6], pickle.loads(rows[0][7]), pickle.loads(rows[0][8]))
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
                    i[5], i[6], pickle.loads(i[7]), pickle.loads(i[8]))
        users.append(user.get_dictionary())
    return users


def update_user(id, nick, password):
    db = get_db()
    cursor = db.cursor()
    user = get_user(id)
    if user == "User does not exist!":
        return "User does not exist!"
    if password is None:
        password = user.password
    if nick is None:
        nick = user.nick
    statement = "UPDATE users SET nick = ?, password = ? WHERE id = ?"
    cursor.execute(statement, [nick, password, id])
    db.commit()
    return True


def delete_user_by_id(id):
    if get_user(id) == "User does not exist!":
        return "User does not exist!"
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

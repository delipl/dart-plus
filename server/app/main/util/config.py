from random import random
from flask import jsonify

from app.main.controller import infoController

DATABASE_NAME = 'database.db'
ID_MAX = 65535
ID_MIN = 50
MESSAGE_OK = "Good"
MESSAGE_ERROR = "Error"
NOT_ACCEPTABLE = 406
INTERNAL_SERVER_ERROR = 500
OK = 200
ERROR_USER_NOT_EXIST = "User does not exist!"
ERROR_GAME_NOT_EXIST = "Game does not exist!"


def generate_http_response(status, message=MESSAGE_ERROR, code=NOT_ACCEPTABLE):
    dictionary = {"status": status, "message": message}
    return jsonify(dictionary), code


def get_dictionary(objects: list):
    dictionary = []
    for i in objects:
        dictionary.append(i.get_dictionary())
    return dictionary


def generate_id():
    id = random.randint(ID_MIN, ID_MAX)
    while infoController.get_user(id) != ERROR_USER_NOT_EXIST:
        id = random.randint(ID_MIN, ID_MAX)
    return id

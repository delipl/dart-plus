import random

from flask import request, jsonify, Blueprint

from app.main.controller import userController
from app.main.util.config import generate_http_response, MESSAGE_OK, OK, \
    INTERNAL_SERVER_ERROR, NOT_ACCEPTABLE, ID_MIN, ID_MAX

userPage = Blueprint('userService', __name__, template_folder='templates')


@userPage.route('/users', methods=["GET"])
def get_users():
    return jsonify(userController.get_users())


@userPage.route("/users", methods=["POST"])
def register():
    user_details = request.json
    id = generate_id()
    password = user_details["password"]
    name = user_details["name"]
    nick = user_details["name"]
    phone = user_details["phone"]
    if userController.get_user_by_phone(phone) != "User does not exist!":
        return generate_http_response(1, "This phone is already use!", NOT_ACCEPTABLE)
    result = userController.insert_user(id, False, password, name, nick, phone, 0, [], [])
    if result:
        return generate_http_response(0, MESSAGE_OK, OK)
    else:
        return generate_http_response(1, "Something wrong with our database :/", INTERNAL_SERVER_ERROR)


@userPage.route("/user", methods=["POST"])
def login():
    user_details = request.json
    phone = user_details["phone"]
    password = user_details["password"]
    user = userController.get_user_by_phone(phone)
    if user == "User does not exist!":
        return generate_http_response(1, "User does not exist!", NOT_ACCEPTABLE)
    if user.password != password:
        return generate_http_response(1, "Incorrect password!", NOT_ACCEPTABLE)
    return generate_http_response(0, "Good", OK)


@userPage.route("/user/<id>", methods=["GET"])
def get_user(id):
    return jsonify(userController.get_user(id).get_dictionary())


@userPage.route("/users", methods=["PUT"])
def update_user():
    user_details = request.json
    id = user_details["id"]
    nick = user_details["nick"]
    password = user_details["password"]

    if password == "empty":
        password = None
    if nick == "empty":
        nick = None

    result = userController.update_user(id, nick, password)
    return generate_http_response(result)


@userPage.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = userController.delete_user(id)
    return generate_http_response(result)

def generate_id():
    id = random.randint(ID_MIN, ID_MAX)
    while userController.get_user(id) != "User does not exist!":
        id = random.randint(ID_MIN, ID_MAX)
    return id
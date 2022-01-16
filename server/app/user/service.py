import random

from flask import request, jsonify, current_app
from . import userPage
from app.user import controller
from config import generate_http_response, Config


# TODO zmien nazwe na auth przepisac od zera z haslem mailem i wszystkim picus glancus
@userPage.route('/users', methods=["GET"])
def get_users():
    return jsonify(controller.get_users())


@userPage.route("/users", methods=["POST"])
def register():
    user_details = request.json
    id = generate_id()
    password = user_details["password"]
    name = user_details["name"]
    nick = user_details["name"]
    phone = user_details["phone"]
    if controller.get_user_by_phone(phone) != "User does not exist!":
        return generate_http_response(1, "This phone is already use!", current_app.config['NOT_ACCEPTABLE'])
    result = controller.insert_user(id, False, password, name, nick, phone, 0, [], [])
    if result:
        return generate_http_response(0, current_app.config['MESSAGE_OK'], current_app.config['OK'])
    else:
        return generate_http_response(1, "Something wrong with our database :/",
                                      current_app.config['INTERNAL_SERVER_ERROR'])


@userPage.route("/user", methods=["POST"])
def login():
    user_details = request.json
    phone = user_details["phone"]
    password = user_details["password"]
    user = controller.get_user_by_phone(phone)
    if user == "User does not exist!":
        return generate_http_response(1, "User does not exist!", current_app.config['NOT_ACCEPTABLE'])
    if user.password != password:
        return generate_http_response(1, "Incorrect password!", current_app.config['NOT_ACCEPTABLE'])
    return generate_http_response(0, "Good", current_app.config['OK'])


@userPage.route("/user/<id>", methods=["GET"])
def get_user(id):
    return jsonify(controller.get_user(id).get_dictionary())


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

    result = controller.update_user(id, nick, password)
    return generate_http_response(result)


@userPage.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = controller.delete_user(id)
    return generate_http_response(result)


def generate_id():
    id = random.randint(current_app.config['ID_MIN'], current_app.config['ID_MAX'])
    while controller.get_user(id) != "User does not exist!":
        id = random.randint(current_app.config['ID_MIN'], current_app.config['ID_MAX'])
    return id

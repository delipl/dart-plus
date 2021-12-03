from flask import request, jsonify

from app import app
from app.main.controller import userController, userController
from app.main.util.config import generate_id, generate_http_response, MESSAGE_OK, OK, \
    INTERNAL_SERVER_ERROR, NOT_ACCEPTABLE


@app.route('/users', methods=["GET"])
def get_users():
    return jsonify(userController.get_users())


@app.route("/users", methods=["POST"])
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


@app.route("/user", methods=["POST"])
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


@app.route("/user/<id>", methods=["GET"])
def get_user(id):
    return jsonify(userController.get_user(id).get_dictionary())


@app.route("/users", methods=["PUT"])
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

@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = userController.delete_user(id)
    return generate_http_response(result)

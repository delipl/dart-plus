import controller
from errors import *
from datetime import datetime
from flask_cors import CORS
from flask import Flask, jsonify, request
from database import create_tables, Settings, Player, generate_id

app = Flask(__name__)
CORS(app)


@app.route('/info/<id>', methods=["GET"])
def get_info(id):
    return jsonify(controller.get_info(id))


@app.route('/games', methods=["GET"])
def get_games():
    return jsonify(controller.get_games())


@app.route("/games/<id>", methods=["DELETE"])
def delete_game(id):
    result = controller.delete_game(id)
    return jsonify(result)


@app.route("/game/<id>", methods=["GET"])
def take_game(id):
    return jsonify(controller.get_game(id).get_dictionary())


# TODO Add online adding new game
@app.route("/games", methods=["POST"])
def insert_new_game():
    id = 1
    game_details = request.json
    gameStatus = game_details["gameStatus"]
    numberOfThrow = game_details["numberOfThrow"]
    startTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    throwingUserId = game_details["throwingUserId"]
    round = game_details["round"]
    setting = game_details["setting"]
    players = []

    result = controller.insert_game(id, gameStatus, numberOfThrow, startTime, throwingUserId, round, setting, players)
    return jsonify(result)


@app.route("/games", methods=["PUT"])
def update_game():
    game_details = request.json
    id = game_details["id"]
    if controller.get_game(id) == ERROR_GAME_NOT_EXIST:
        return "Game not exist"
    status = game_details["status"]
    throwingPlayerId = game_details["throwingPlayerId"]
    lastThrow = game_details["lastThrow"]
    round = game_details["round"]
    playerList = game_details["playerList"]

    result = controller.update_game(id, status, throwingPlayerId, lastThrow["multiplier"], lastThrow["value"], round,
                                    playerList)
    return jsonify(result)


@app.route("/settings", methods=["POST"])
def create_new_game():
    setting_details = request.json
    id = setting_details["id"]
    numberOfPlayers = setting_details["numberOfPlayers"]
    startPoints = setting_details["startPoints"]
    doubleIn = setting_details["doubleIn"]
    doubleOut = setting_details["doubleOut"]
    playersId = setting_details["playersId"]

    setting = Settings(numberOfPlayers, startPoints, doubleIn, doubleOut)
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    players = []

    for i in range(numberOfPlayers):
        players.append(Player(playersId[i], "Gracz" + str(i + 1), startPoints, 0))

    result = controller.insert_game(id, 0, 0, date, playersId[0], 0, setting, players)
    return jsonify(result)


@app.route('/users', methods=["GET"])
def get_users():
    return jsonify(controller.get_users())


# TODO Add encrypt and decrypt password
# TODO Add id to hex > TEXT
@app.route("/users", methods=["POST"])
def insert_user():
    dictionary = {}
    user_details = request.json
    id = generate_id()
    password = user_details["password"]
    name = user_details["name"]
    nick = user_details["name"]
    phone = user_details["phone"]
    if controller.get_user_phone(phone) != ERROR_USER_NOT_EXIST:
        dictionary["status"] = 1
        dictionary["message"] = "This phone is already use!"
        return jsonify(dictionary), 404
    maxThrow = 0
    throws = []
    average = 0
    wins = 0
    gameIds = []
    result = controller.insert_user(id, password, name, nick, phone, maxThrow, throws, average, wins, gameIds)
    if result:
        dictionary["status"] = 0
        dictionary["message"] = "Good"
        return jsonify(dictionary), 200
    else:
        dictionary["status"] = 1
        dictionary["message"] = "Something wrong with our database :/"
        return jsonify(dictionary), 404


@app.route("/user", methods=["POST"])
def login():
    dictionary = {}
    user_details = request.json
    phone = user_details["phone"]
    password = user_details["password"]
    user = controller.get_user_phone(phone)
    if user == ERROR_USER_NOT_EXIST:
        dictionary["status"] = 1
        dictionary["message"] = "User does not exist!"
        return jsonify(dictionary), 404
    if user.password != password:
        dictionary["status"] = 1
        dictionary["message"] = "Incorrect password!"
        return jsonify(dictionary), 404
    dictionary["status"] = 0
    dictionary["message"] = "Good"
    return jsonify(dictionary), 200


@app.route("/user/<id>", methods=["GET"])
def get_user(id):
    return jsonify(controller.get_user(id).get_dictionary())


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

    result = controller.update_user(id, nick, password)
    return jsonify(result)


@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = controller.delete_user(id)
    return jsonify(result)


if __name__ == "__main__":
    create_tables()
    #print(controller.delete_users())
    #print(controller.delete_games())
    app.run(host='0.0.0.0', port=8000, debug=False)

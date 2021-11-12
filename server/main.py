from datetime import datetime

from flask import Flask, jsonify, request
import controller
from database import create_tables, Settings

app = Flask(__name__)


@app.route('/games', methods=["GET"])
def get_games():
    return jsonify(controller.get_games())


@app.route('/users', methods=["GET"])
def get_users():
    return jsonify(controller.get_users())


@app.route("/games", methods=["POST"])
def insert_game():
    game_details = request.json
    gameStatus = game_details["gameStatus"]
    maxThrow = game_details["maxThrow"]
    numberOfThrow = game_details["numberOfThrow"]
    startTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    throwingUserId = game_details["throwingUserId"]
    round = game_details["round"]
    setting = game_details["setting"]

    result = controller.insert_games(gameStatus, maxThrow, numberOfThrow, startTime, throwingUserId, round, setting)
    return jsonify(result)


@app.route("/users", methods=["POST"])
def insert_user():
    user_details = request.json
    name = user_details["name"]
    nick = user_details["nick"]
    maxThrow = user_details["maxThrow"]
    throws = user_details["throws"]
    average = user_details["average"]
    wins = user_details["wins"]
    matches = user_details["matches"]
    result = controller.insert_user(name, nick, maxThrow, throws, average, wins, matches)
    return jsonify(result)


@app.route("/game/<id>", methods=["PUT"])
def update_game(id):
    game_details = request.json
    gameStatus = game_details["gameStatus"]
    maxThrow = game_details["maxThrow"]
    numberOfThrow = game_details["numberOfThrow"]
    throwingUserId = game_details["throwingUserId"]
    round = game_details["round"]
    setting = game_details["setting"]
    result = controller.update_game(id, gameStatus, maxThrow, numberOfThrow,
                                    controller.get_games()[0]["startTime"], throwingUserId, round, setting)
    return jsonify(result)


@app.route("/game/<id>", methods=["GET"])
def take_game(id):
    return jsonify(controller.get_game(id))


@app.route("/user/<id>", methods=["GET"])
def take_user(id):
    return jsonify(controller.get_user(id))


@app.route("/user/<id>", methods=["PUT"])
def update_user(id):
    user_details = request.json
    name = user_details["name"]
    nick = user_details["nick"]
    maxThrow = user_details["maxThrow"]
    throws = user_details["throws"]
    average = user_details["average"]
    wins = user_details["wins"]
    matches = user_details["matches"]
    result = controller.update_user(id, name, nick, maxThrow, throws, average, wins, matches)
    return jsonify(result)


@app.route("/games/<id>", methods=["DELETE"])
def delete_game(id):
    result = controller.delete_game(id)
    return jsonify(result)


@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    result = controller.delete_user(id)
    return jsonify(result)


if __name__ == "__main__":
    create_tables()
    # print(controller.insert_user("Bartosz", "Barto", 180, 33, 36.5, 12, 90))
    #print(controller.delete_users())
    #print(controller.delete_games())
    #print(controller.insert_games(1, 132, 12, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 33, 0, Settings(2, 301, False, False)))
    app.run(host='0.0.0.0', port=8000, debug=True)

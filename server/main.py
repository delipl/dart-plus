from flask import Flask, jsonify, request
import controller
from database import create_tables
from datetime import datetime

app = Flask(__name__)


# HTTP GET | At /settings list setting db tables
@app.route('/settings', methods=["GET"])
def get_settings():
    return jsonify(controller.get_settings())


@app.route('/players', methods=["GET"])
def get_players():
    return jsonify(controller.get_players())


# HTTP POST | create new setting/ mean new game start
@app.route("/settings", methods=["POST"])
def insert_setting():
    setting_details = request.json
    gameStatus = setting_details["gameStatus"]
    maxThrow = setting_details["maxThrow"]
    numberOfThrow = setting_details["numberOfThrow"]
    startTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    throwingPlayerId = setting_details["throwingPlayerId"]
    round = setting_details["round"]
    result = controller.insert_settings(gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round)
    return jsonify(result)


# HTTP POST | create new player
@app.route("/players", methods=["POST"])
def insert_player():
    player_details = request.json
    name = player_details["name"]
    nick = player_details["nick"]
    maxThrow = player_details["maxThrow"]
    throws = player_details["throws"]
    average = player_details["average"]
    wins = player_details["wins"]
    matches = player_details["matches"]
    result = controller.insert_player(name, nick, maxThrow, throws, average, wins, matches)
    return jsonify(result)


@app.route("/settings/<id>", methods=["PUT"])
def update_setting(id):
    setting_details = request.json
    gameStatus = setting_details["gameStatus"]
    maxThrow = setting_details["maxThrow"]
    numberOfThrow = setting_details["numberOfThrow"]
    throwingPlayerId = setting_details["throwingPlayerId"]
    round = setting_details["round"]
    result = controller.update_setting(id, gameStatus, maxThrow, numberOfThrow,
                                       controller.get_settings()[0]["startTime"], throwingPlayerId, round)
    return jsonify(result)


@app.route("/player/<id>", methods=["PUT"])
def update_player(id):
    player_details = request.json
    name = player_details["name"]
    nick = player_details["nick"]
    maxThrow = player_details["maxThrow"]
    throws = player_details["throws"]
    average = player_details["average"]
    wins = player_details["wins"]
    matches = player_details["matches"]
    result = controller.update_player(id, name, nick, maxThrow, throws, average, wins, matches)
    return jsonify(result)


# After end game delete this element
@app.route("/settings/<id>", methods=["DELETE"])
def delete_setting(id):
    result = controller.delete_settings(id)
    return jsonify(result)


if __name__ == "__main__":
    create_tables()
    # print(controller.insert_player("Bartosz", "Barto", 180, 33, 36.5, 12, 90))
    # print(controller.delete_players())
    # print(controller.insert_settings(1, 132, 12, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 33, 0))
    app.run(host='0.0.0.0', port=8000, debug=True)

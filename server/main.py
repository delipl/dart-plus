from flask import Flask, jsonify, request
import controller
from database import create_tables

app = Flask(__name__)


# HTTP GET | At /settings list setting db tables
@app.route('/settings', methods=["GET"])
def get_games():
    games = controller.get_settings()
    return jsonify(games)


# HTTP POST | create new setting/ mean new game start
@app.route("/settings", methods=["POST"])
def insert_game():
    setting_details = request.get_json()
    gameStatus = setting_details["gameStatus"]
    maxThrow = setting_details["maxThrow"]
    numberOfThrow = setting_details["numberOfThrow"]
    startTime = setting_details["startTime"]
    throwingPlayerId = setting_details["throwingPlayerId"]
    round = setting_details["round"]

    result = controller.insert_settings(gameStatus, maxThrow, numberOfThrow, startTime, throwingPlayerId, round)
    return jsonify(result)


@app.after_request
def after_request(response):
    response.headers[
        "Access-Control-Allow-Origin"] = "*"  # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers[
        "Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    create_tables()
    print(controller.insert_settings(0, 0, 0, "test", 1, 1))
    app.run(host='0.0.0.0', port=8000, debug=False)

from flask import jsonify

MESSAGE_OK = "Good"
MESSAGE_ERROR = "Error"
NOT_ACCEPTABLE = 406
INTERNAL_SERVER_ERROR = 500
OK = 200


def generate_http_response(status, message=MESSAGE_ERROR, code=NOT_ACCEPTABLE):
    dictionary = {"status": status, "message": message}
    return jsonify(dictionary), code


ERROR_USER_NOT_EXIST = "User does not exist!"
ERROR_GAME_NOT_EXIST = "Game does not exist!"

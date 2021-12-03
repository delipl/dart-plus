import random

from flask import jsonify

ID_MAX = 65535
ID_MIN = 50
MESSAGE_OK = "Good"
MESSAGE_ERROR = "Error"
NOT_ACCEPTABLE = 406
INTERNAL_SERVER_ERROR = 500
OK = 200


def generate_http_response(status, message=MESSAGE_ERROR, code=NOT_ACCEPTABLE):
    dictionary = {"status": status, "message": message}
    return jsonify(dictionary), code


def get_dictionary(objects: list):
    dictionary = []
    for i in objects:
        dictionary.append(i.get_dictionary())
    return dictionary


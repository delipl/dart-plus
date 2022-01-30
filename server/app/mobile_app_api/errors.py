from flask import jsonify
from app.exceptions import ValidationError
from app.dart_board_api import dartBordApi


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message, 'status': 0})
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


@dartBordApi.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])

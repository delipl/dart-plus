from flask import request, jsonify

from app.info import controller
from . import infoPage


# TODO Do przebudowania cale !!!!!
@infoPage.route('/info', methods=["GET"])
def get_info():
    return jsonify(controller.get_info(1))



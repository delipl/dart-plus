from flask import request, jsonify, Blueprint

from app.main.controller import infoController

infoPage = Blueprint('infoService', __name__, template_folder='templates')


@infoPage.route('/info', methods=["GET"])
def get_info():
    return jsonify(infoController.get_info(1))



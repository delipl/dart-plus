import random

from flask import request, jsonify, current_app
from . import userPage
from app.user import controller
from config import generate_http_response, Config
from app.models.user import User


@userPage.route('/', methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify({'users': [user.to_json() for user in users]})





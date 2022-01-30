from flask import render_template, current_app, url_for, request, g, jsonify
from flask_httpauth import HTTPBasicAuth

import base64
import app
from app import db
from . import mobileApp
from ..models.user import User
from flask_login import login_user, logout_user, login_required, current_user
from config import generate_http_response
from .errors import unauthorized, forbidden
import base64

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(phone_or_token, password):
    if phone_or_token == '':
        return False
    if password == '':
        g.current_user = User.verify_auth_token(phone_or_token)
        return g.current_user is not None
    user = User.query.filter_by(phone=phone_or_token.lower()).first()
    if not user:
        return False
    g.current_user = user
    return user.verify_password(password)


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


@mobileApp.route('/token', methods=['GET', 'POST'])
@auth.login_required
def get_token():
    if g.current_user.is_anonymous:
        return unauthorized('Invalid credentials')
    return jsonify({'token': g.current_user.generate_auth_token(
        expiration=360000), 'expiration': 360000, 'status': 1, 'message': ''})


# dezaktywacja

@mobileApp.route('/register', methods=['POST'])
def register():
    # phone = request.json.get('phone')
    phone = base64.b64decode(request.json.get('phone')).decode('utf-8')
    # password = request.json.get('password')
    password = base64.b64decode(request.json.get('password')).decode('utf-8')
    name = request.json.get('name')
    nick = request.json.get('nick')

    if User.query.filter_by(phone=phone).first() is not None:
        return generate_http_response(False, "PHONE NUMBER IS ALREADY USED", 400)

    if User.query.filter_by(name=name).first() is not None:
        return generate_http_response(False, "NAME IS ALREADY USED", 400)

    user = User(phone=phone, name=name, password=password, nick=name, attempts=0, points=301)

    db.session.add(user)
    db.session.commit()
    return generate_http_response(True, "OK", 200)


# @mobileApp.route('/login', methods=['GET', 'POST'])
# def login():
#     password = request.json.get('password')
#     print(password)
#     # password = base64.b64decode(request.json.get('password')).decode('utf-8')
#     user = User.query.filter_by(phone=request.json.get('phone')).first()
#     print(user)
#
#     if user is not None and user.verify_password(password):
#         login_user(user)
#         print(current_user)
#         return generate_http_response(True, "OK", 200)
#     return generate_http_response(False, "Unsuccesful login", 401)
#
#
# @mobileApp.route('/logout', methods=['GET'])
# @login_required
# def logout():
#     logout_user()
#     return generate_http_response(True, "OK", 200)
#
#

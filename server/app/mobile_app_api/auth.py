import datetime

import jwt
from flask import render_template, current_app, url_for, request, g, jsonify

import app
from app import db
import os
from . import mobileApp
from ..models.user import User
from flask_login import login_user, logout_user, login_required, current_user
from config import generate_http_response


@mobileApp.route('/login', methods=['GET', 'POST'])
def login():
    user = User.query.filter_by(phone=request.json.get('phone')).first()
    if user is not None and user.verify_password(request.json.get('password')):
        login_user(user)
        token = jwt.encode({'user': user.name, 'exp': datetime.datetime.utcnow() +
                           datetime.timedelta(minutes=30)}, current_app.config['SECRET_KEY'])
        return jsonify({'token': token})

    return generate_http_response(False, "Unsuccesful login", 401)


@mobileApp.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return generate_http_response(True, "OK", 200)


@mobileApp.route('/register', methods=['GET', 'POST'])
def register():
    phone = request.json.get('phone')
    password = request.json.get('password')
    name = request.json.get('name')
    nick = request.json.get('nick')

    if User.query.filter_by(phone=phone).first() is not None:
        return generate_http_response(False, "PHONE NUMBER IS ALREADY USED", 400)

    if User.query.filter_by(name=name).first() is not None:
        return generate_http_response(False, "NAME IS ALREADY USED", 400)

    user = User(phone=phone, name=name, password=password, nick=nick)

    db.session.add(user)
    db.session.commit()
    return generate_http_response(True, "OK", 200)

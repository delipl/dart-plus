from flask import render_template, redirect, url_for, request, flash
from app import db
import os
from . import auth
from ..models.user import User
from flask_login import login_user, logout_user, login_required, current_user
from config import generate_http_response


@auth.route('/login', methods=['GET', 'POST'])
def login():
    user = User.query.filter_by(phone=request.json.get('phone')).first()
    if user is not None and user.verify_password(request.json.get('password')):
        login_user(user)
    return generate_http_response(True, "OK", 200)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return generate_http_response(True, "OK", 200)


# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     phone = request.json.get('phone')
#     password_hash = request.json.get('password')
#     if form.validate_on_submit():
#         user = User(email=form.email.data, username=form.username.data,
#                     password=form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         token = user.generate_confirmation_token()
#         send_email(user.email, "verify your account",
#                    'auth/email/confirm', user=user, token=token)
#         flash('on your email we sent verification message')
#         os.mkdir('/home/ziolko/fluskProjects/Blog/app/static/' + user.username)
#         return redirect(url_for('auth.login'))
#     return render_template('auth/register.html', form=form)
#
#
# @auth.route('/confirm/<token>')
# @login_required
# def confirm(token):
#     if current_user.confirmed:
#         return redirect(url_for('main.index'))
#     if current_user.confirm(token):
#         db.session.commit()
#         flash('You has been verified')
#     else:
#         flash('Link is not correct')
#     return redirect(url_for('main.index'))
#
#
# @auth.before_app_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.ping()
#         if not current_user.confirmed \
#                 and request.blueprint != 'auth' and request.endpoint != 'static':
#             return redirect(url_for('auth.unconfirmed'))
#
#
# @auth.route('/unconfirmed')
# def unconfirmed():
#     if current_user.is_anonymous or current_user.confirmed:
#         return redirect(url_for('main.index'))
#     return render_template('auth/unconfirmed.html')
#
#
# @auth.route('/confirm')
# @login_required
# def resend_confirmation():
#     token = current_user.generate_confirmation_token()
#     send_email(current_user.email, "verify your account",
#                'auth/email/confirm', user=current_user, token=token)
#     flash('we resent verification message')
#     return redirect(url_for('main.index'))

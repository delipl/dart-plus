import base64
import json
import unittest
from unittest.mock import patch
from flask import g
from flask_login import current_user

from app import create_app, db
from app.models.user import User, user_game
from app.models.game import Game
from app.models.dart_board import DartBoard


class GameApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app, socketio = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        # Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

        dartBoard = DartBoard()
        db.session.add(dartBoard)
        artur = User(name='Artur', phone='123456780', password='huj', nick='louda', wins='2137', board=dartBoard)
        bartek = User(name='Bartek', phone='123456789', password='huj', nick='la', wins='69', board=dartBoard)
        kuba = User(name='Kuba', phone='123456788', password='huj', nick='uda', wins='420', board=dartBoard)
        db.session.add(artur)
        db.session.add(bartek)
        db.session.add(kuba)
        game = Game(startPoints='301')
        game.board = dartBoard
        db.session.add(game)
        artur.active_games.append(game)
        bartek.active_games.append(game)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_login_success(self):
        # password = "huj".encode("utf-8")
        # password = base64.b64encode(password)
        # print(password)
        data = json.dumps(
            {
                "phone": 123456789,
                "password": 'huj'
            })


        headers = {'Content-Type': 'application/json'}

        with self.client:
            response = self.client.post('/mobileApp/login', headers=headers, data=data)
            self.assertEqual(current_user.name, 'Bartek')
            self.assertEqual(response.status_code, 200)

    def test_login_not_success(self):
        data = json.dumps(
            {
                "phone": 133456789,
                "password": 'huj'
            })

        headers = {'Content-Type': 'application/json'}

        with self.client:
            response = self.client.post('/mobileApp/login', headers=headers, data=data)
            self.assertEqual(response.status_code, 401)

    def test_registration_success(self):
        data = json.dumps(
            {
                "phone": 133456789,
                "password": 'huj',
                "name": 'jan',
                "nick": 'kowalski'
            })

        headers = {'Content-Type': 'application/json'}

        with self.client:
            response = self.client.post('/mobileApp/register', headers=headers, data=data)
            self.assertEqual(response.status_code, 200)
            user = User.query.filter_by(name='jan').first()
            self.assertEqual(user.name, 'jan')

    def test_registration_not_success_used_phone(self):
        data = json.dumps(
            {
                "phone": 123456789,
                "password": 'huj',
                "name": 'jan',
                "nick": 'kowalski'
            })

        headers = {'Content-Type': 'application/json'}

        with self.client:
            response = self.client.post('/mobileApp/register', headers=headers, data=data)
            self.assertEqual(response.status_code, 400)

    def test_login_required(self):
        with self.client:
            response = self.client.get('/mobileApp/')
            self.assertEqual(response.status_code, 302)
            data = json.dumps(
                {
                    "phone": 123456789,
                    "password": 'huj'
                })

            headers = {'Content-Type': 'application/json'}
            response = self.client.post('/mobileApp/login', headers=headers, data=data)
            response = self.client.get('/mobileApp/')
            self.assertEqual(response.status_code, 200)



    # def test_create_new_game(self):
    #     data = json.dumps(
    #         {
    #             "startPoints": 301,
    #             "doubleOut": False,
    #             "doubleIn": True,
    #             "playersId": [1, 2]
    #         })
    #
    #     headers = {'Content-Type': 'application/json'}
    #
    #     response = self.client.post('/games/', headers=headers, data=data)
    #     self.assertEqual(response.status_code, 200)
    #     game = Game.query.get_or_404(2)
    #     self.assertEqual(game.startPoints, 301)
    #     self.assertEqual([player.id for player in game.players], [1, 2])
    #     self.assertEqual(game.doubleIn, True)
    #     self.assertEqual(game.doubleOut, False)

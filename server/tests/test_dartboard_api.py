import json
import unittest

from flask_socketio import SocketIO

from app import create_app, db
from app.dart_board_api.game_socket_room import GameSocketRoom
from app.models.user import User, user_game
from app.models.game import Game
from app.models.dart_board import DartBoard


class DartboardApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        socketio = SocketIO(self.app, cors_allowed_origins='*')
        socketio.on_namespace(GameSocketRoom('/esp'))
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

    def test_get_settings(self):
        data = json.dumps(
            {
                "board_id": 1
            })

        headers = {'Content-Type': 'application/json'}

        response = self.client.post('/dartBoard/settings', headers=headers, data=data)
        self.assertEqual(response.status_code, 200)
        game = DartBoard.query.get_or_404(1).games[0]
        self.assertEqual(game.id, response.json.get('id'))
        self.assertEqual(game.doubleIn, response.json.get('doubleIn'))
        self.assertEqual(game.doubleOut, response.json.get('doubleOut'))
        self.assertEqual(game.startPoints, response.json.get('startPoints'))
        i = 0
        for player in response.json.get('players'):
            self.assertEqual(game.players[i].board_id, player['board_id'])
            self.assertEqual(game.players[i].nick, player['nick'])
            self.assertEqual(game.players[i].id, player['id'])
            i += 1

        # json_post = {
        #     "id": self.id,
        #     "startPoints": self.startPoints,
        #     "doubleIn": self.doubleIn,
        #     "doubleOut": self.doubleOut,
        #     "players": [player.player_to_json_setting() for player in self.players]
        # }


    #
    # def test_delete_games(self):
    #     self.assertTrue(len(Game.query.all()) != 0)
    #     response = self.client.delete('/games/1')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(len(Game.query.all()) == 0)
    #
    # def test_get_game_by_id(self):
    #     response = self.client.get('/games/1')
    #     game = Game.query.first()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.get_data(as_text=True),
    #                     '{\"doubleIn\":false,\"doubleOut\":false,\"gameStatus\":null,\"id\":1,\"round\":null,\"startPoints\":301,\"startTime\":' + "\"" + game.startTime.strftime("%m/%d/%Y, %H:%M:%S") + "\"" + ',\"throwingUserId\":null,\"users_id\":[1,2]}\n')
    #
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
    #
    # def test_update_game(self):
    #     data = json.dumps(
    #         {
    #             "id": 1,
    #             "status": 1,
    #             "round": 1,
    #             "value": 10,
    #             "multiplier": 2,
    #             "throwingPlayerId": 1,
    #             "throwingUserId": 1,
    #             "players": [
    #                 {
    #                     "id": 1,
    #                     "attempts": 1,
    #                     "points": 229
    #                 },
    #                 {
    #                     "id": 2,
    #                     "attempts": 5,
    #                     "points": 259
    #                 }
    #             ]
    #         })
    #
    #     headers = {'Content-Type': 'application/json'}
    #     response = self.client.put('/games/', headers=headers, data=data)
    #     self.assertEqual(response.status_code, 200)
    #     game = Game.query.get_or_404(1)
    #     player_1 = User.query.get_or_404(1)
    #     player_2 = User.query.get_or_404(2)
    #     self.assertEqual(game.startPoints, 301)
    #     self.assertEqual(player_1.throws[0].value, 10)
    #     self.assertEqual(player_1.throws[0].multiplier, 2)
    #     self.assertEqual(player_1.points, 229)
    #     self.assertEqual(player_2.points, 259)
    #
    #     response = self.client.put('/games/', headers=headers, data=data)
    #     self.assertEqual(player_1.throws[1].value, 10)
    #     self.assertEqual(player_1.throws[1].multiplier, 2)


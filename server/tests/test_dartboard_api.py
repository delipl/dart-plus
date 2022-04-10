import json
import unittest

from flask_socketio import SocketIO

from app import create_app, db
from app.dart_board_api.game_socket_esp import GameSocketEsp
from app.models.user import User, user_game
from app.models.game import Game
from app.models.dart_board import DartBoard


class DartboardApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app, self.socketio = create_app('testing')
        socketio = SocketIO(self.app, cors_allowed_origins='*')
        socketio.on_namespace(GameSocketEsp('/esp'))
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        # Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

        dartBoard = DartBoard()
        dartboard2 = DartBoard()
        db.session.add(dartBoard)
        artur = User(name='Artur', phone='123456780', password='huja', nick='louda', wins='2137', board=dartBoard)
        bartek = User(name='Bartek', phone='123456789', password='huja', nick='la', wins='69', board=dartBoard)
        kuba = User(name='Kuba', phone='123456788', password='huja', nick='uda', wins='420', board=dartboard2)
        db.session.add(artur)
        db.session.add(bartek)
        db.session.add(kuba)
        db.session.commit()
        game = Game(startPoints='301')
        game.boards.append(dartBoard)
        game.boards.append(dartboard2)
        db.session.add(game)
        db.session.commit()

        artur.active_games.append(game)
        bartek.active_games.append(game)
        kuba.active_games.append(game)
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
        game = DartBoard.query.get_or_404(1).game
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

    def test_game_socket_room(self):
        client = self.socketio.test_client(self.app, namespace='/esp')
        payload = {'game_id': 1}
        client.connect()
        data = {
            "id": 1,
            "status": 1,
            "round": 1,
            "value": 10,
            "multiplier": 2,
            "throwingPlayerId": 1,
            "throwingUserId": 1,
            "players": [
                {
                    "id": 1,
                    "attempts": 1,
                    "points": 229,
                    "nick": "jj",
                    "board_id": 1
                },
                {
                    "id": 2,
                    "nick": "jj",
                    "board_id": 1,
                    "attempts": 3,
                    "points": 259
                }
            ]
        }
        client.emit('game_loop', data, namespace='/esp')
        game = Game.query.get_or_404(1)

        self.assertEqual(game.gameStatus, 1)
        self.assertEqual(game.throwingUserId, 1)
        self.assertEqual(game.round, 1)

        player1 = User.query.get_or_404(1)
        self.assertEqual(player1.points, 229)
        self.assertEqual(player1.attempts, 1)

        player2 = User.query.get_or_404(2)
        self.assertEqual(player2.points, 259)
        self.assertEqual(player2.attempts, 3)


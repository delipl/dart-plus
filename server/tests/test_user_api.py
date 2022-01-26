import json
import unittest

from app import create_app, db
from app.models.user import User, user_game
from app.models.game import Game
from app.models.dart_board import DartBoard


class UserApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app, socketio = create_app('testing')
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

    def test_get_users(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

        # self.assertEqual(response.get_data(as_text=True),
        #                 '{\"users\":[{\"attempts\":null,\"games_id\":[1],\"id\":1,\"name\":\"Artur\",\"nick\":\"louda\",\"password\":\"pbkdf2:sha256:150000$lfpJBpY9$baa59aa09ce609e2c7bfc4042ca17118581c698946a0428734fe298c05af6f8c\",\"phone\":123456780,\"throws\":[],\"wins\":2137},{\"attempts\":null,\"games_id\":[1],\"id\":2,\"name\":\"Bartek\",\"nick\":\"la\",\"password\":\"pbkdf2:sha256:150000$92nvX7tq$21d06a0f58eb2fa1d0317a348f8d8e41e4fef50b6525e62b5f39eda7b376c47a\",\"phone\":123456789,\"throws\":[],\"wins\":69},{\"attempts\":null,\"games_id\":[],\"id\":3,\"name\":\"Kuba\",\"nick\":\"uda\",\"password\":\"pbkdf2:sha256:150000$VbsIm207$018ff98917644f1b723a23e0db1552fbbc297464cbf3e01907e0987fdad293eb\",\"phone\":123456788,\"throws\":[],\"wins\":420}]}')

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


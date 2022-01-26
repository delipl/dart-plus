from flask_login import current_user
from flask_socketio import send, Namespace, emit, join_room, leave_room
from flask import request, current_app

from app import db
from app.models.game import Game
from app.models.throw import Throw
from app.models.user import User
from config import config


class GameSocketApp(Namespace):

    def run(self):
        pass

    def on_connect(self):
        print("connected with", request.sid)

    def on_disconnect(self):
        pass

    def on_join_room(self):
        sid = request.sid
        gameid = '1'
        room_name = '/' + gameid
        join_room(room_name)
        print(sid + ' has enter the room.')
        game = Game.query.get_or_404(1)
        payload = game.get_settings_to_json()
        send(payload, to=room_name)

    def on_leave_room(self, data):
        sid = request.sid
        gameid = '1'
        room_name = '/' + gameid
        leave_room(room_name)
        print(sid + 'has left the room.')
        game = Game.query.get_or_404(1)
        payload = game.get_settings_to_json()
        emit(payload, to=room_name)

    def on_game_update(self):
        players_without_current = []
        for player in Game.query.get_or_404(1).players:
            if player.id != current_user.id:
                players_without_current.append(player)

        payload = {
            "attempts": current_user.attempts,
            "points": current_user.points,
            "nick": current_user.nick,
            "players": [player.player_to_json_game_update() for player in players_without_current]
        }
        print(payload)

        send(payload, to=request.sid)


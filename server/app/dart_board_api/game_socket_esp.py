from flask_socketio import send, Namespace, emit, join_room, leave_room
from flask import request, current_app

from app import db
from app.models.game import Game
from app.models.throw import Throw
from app.models.user import User
from config import config


class GameSocketEsp(Namespace):

    def run(self):
        pass

    def on_connect(self):
        print("connected with", request.sid)

    def on_disconnect(self):
        print("disconect with", request.sid)

    def on_join_room(self, data):
        sid = request.sid
        gameid = str(data["game_id"])
        game = Game.query.get_or_404(gameid)
        room_name = current_app.config['ROOM_NAME'] + gameid
        join_room(room_name)
        print(sid + ' has enter the room.')
        print(game.throwingUserId)

        current_player = User.query.get_or_404(game.throwingUserId)
        payload = {
            'id': game.id,
            'status': game.gameStatus,
            'throwingPlayerId': current_player.id,
            'multiplier': 0,
            'value': 0,
            'startPoints': game.startPoints,
            'doubleIn': game.doubleIn,
            "doubleOut": game.doubleOut,
            'round': game.round,
            'players': [player.player_to_json_game_loop() for player in game.players]}

        emit('game_loop', payload, to=request.sid)
        # send(payload, to=request.sid)

    def on_leave_room(self, data):
        sid = request.sid
        gameid = str(data["game_id"])
        room_name = current_app.config['ROOM_NAME'] + gameid
        leave_room(room_name)
        print(sid + 'has left the room.')

    def on_game_loop(self, data):
        print(data)
        gameid = str(data["id"])

        print(f"game id is {gameid}.")
        room_name = current_app.config['ROOM_NAME'] + str(gameid)
        gamestatus = str(data["status"])

        game_id = data['id']
        status = data['status']
        throwingPlayerId = data['throwingPlayerId']
        multiplier = data['multiplier']
        value = data['value']
        print(f"value is {value}.")
        round = data['round']
        players = data['players']
        players_id = [player['id'] for player in players]
        players_attempts = [player['attempts'] for player in players]
        players_nick = [player['nick'] for player in players]
        players_board_id = [player['board_id'] for player in players]
        players_points = [player['points'] for player in players]

        users = [User.query.get_or_404(player_id) for player_id in players_id]
        for i in range(len(users)):
            users[i - 1].attempts = players_attempts[i - 1]
            users[i - 1].points = players_points[i - 1]

        users[throwingPlayerId - 1].throws_multiplier = multiplier
        users[throwingPlayerId - 1].throws_value = value
        throw = Throw(value=value, multiplier=multiplier, player=users[throwingPlayerId - 1])
        db.session.add(throw)
        game = Game.query.get_or_404(game_id)
        game.gameStatus = status
        game.throwingUserId = throwingPlayerId
        game.round = round
        db.session.commit()

        room_name_app = '/' + gameid
        current_player = User.query.get_or_404(game.throwingUserId)
        players_without_current = []
        for player in game.players:
            if player.id != current_player.id:
                players_without_current.append(player)
        payload = {
            'attempts': current_player.attempts,
            'points': current_player.points,
            'nick': current_player.nick,
            'players': [player.player_to_json_game_update() for player in players_without_current]}

        emit('game_loop', payload, to=room_name_app, namespace="/app")
        emit('game_loop', data, to=room_name, skip_sid=request.sid)
        # send(data, to=room_name, skip_sid=request.sid)


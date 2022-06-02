from flask_socketio import send, Namespace, emit, join_room, leave_room
from flask import request, current_app, g

from app import db
from app.models.game import Game
from app.models.throw import Throw
from app.models.user import User
from config import config


class GameLoopSocket(Namespace):

    def run(self):
        pass

    def on_connect(self):
        print("connected with", request.sid)

    def on_disconnect(self):
        print("disconect with", request.sid)

    def on_join_room(self, data):
        print('room has been joined')

        print(data)

        is_esp = data["is_esp"]
        sid = request.sid
        gameid = data["game_id"]

        game = Game.query.get_or_404(gameid)
        room_name = current_app.config['ROOM_NAME'] + str(gameid)
        join_room(room_name)
        print(sid + ' has enter the esp_room.')
        if is_esp:
            current_player = User.query.get_or_404(game.throwingUserId)
            payload = {
                'id': game.id,
                'status': game.gameStatus,
                'throwingPlayerId': current_player.id,
                'multiplier': 0,
                'value': 0,
                'startPoints': game.startPoints,
                'doubleIn': game.doubleIn,
                'doubleOut': game.doubleOut,
                'round': game.round,
                'players': [player.player_to_json_game_loop() for player in game.players]}

            emit('game_loop', payload, to=request.sid)
        else:
            phone = str(data['phone'])
            g.current_user = User.query.filter_by(phone=phone).first()
            current_player = User.query.get_or_404(game.throwingUserId)
            players_without_current = []
            for player in game.players:
                if player.id != g.current_user.id:
                    players_without_current.append(player)

            payload = {
                'attempts': current_player.attempts,
                'points': current_player.points,
                'nick': current_player.nick,
                'players': [player.player_to_json_game_update() for player in players_without_current]}

            emit('game_loop', payload, to=request.sid)


    def on_leave_room(self, data):
        sid = request.sid
        gameid = str(data["game_id"])
        room_name = current_app.config['ROOM_NAME'] + gameid
        leave_room(room_name)
        print(sid + 'has left the esp_room.')

    def on_game_loop_esp(self, data):
        print(data)
        gameid = str(data["id"])
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

        emit('game_loop_app', payload, to=room_name)
        emit('game_loop_esp', data, to=room_name, skip_sid=request.sid)
        # send(data, to=room_name, skip_sid=request.sid)

    def on_game_loop_app(self, data):
        # current user we do not know
        gameid = str(data['game_id'])
        room_name = '/' + gameid
        phone = str(data['phone'])
        g.current_payer = User.query.filter_by(phone=phone).first()
        game = Game.query.get_or_404(gameid)

        players_without_current = []
        for player in game.players:
            if player.id != g.current_user.id:
                players_without_current.append(player)

        payload = {
            "attempts": g.current_user.attempts,
            "points": g.current_user.points,
            "nick": g.current_user.nick,
            "players": [player.player_to_json_game_update() for player in players_without_current]
        }
        print(payload)

        emit('game_loop', payload, to=room_name)

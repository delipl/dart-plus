# TO DELETE


# from flask_login import current_user
# from flask_socketio import send, Namespace, emit, join_room, leave_room
# from flask import request, current_app, g
# from app.models.game import Game
# from app.models.user import User
#
#
# class GameSocketApp(Namespace):
#
#     def run(self):
#         pass
#
#     def on_connect(self):
#         print("connected with", request.sid)
#
#     def on_disconnect(self):
#         pass
#
#     def on_join_room_app(self, data):
#         print(data)
#         sid = request.sid
#         gameid = str(data["game_id"])
#         phone = str(data['phone'])
#         if phone != 0:
#             g.current_user = User.query.filter_by(phone=phone).first()
#         else:
#             g.current_user = None
#         print(g.current_user)
#         room_name = '/' + gameid
#         join_room(room_name)
#         print(sid + ' has enter the room.')
#         game = Game.query.get_or_404(gameid)
#         print(game.players)
#         print(game.throwingUserId)
#         current_player = User.query.get_or_404(game.throwingUserId)
#         players_without_current = []
#         for player in game.players:
#             if player.id != g.current_user.id:
#                 players_without_current.append(player)
#
#         payload = {
#             'attempts': current_player.attempts,
#             'points': current_player.points,
#             'nick': current_player.nick,
#             'players': [player.player_to_json_game_update() for player in players_without_current]}
#
#         emit('game_loop', payload, to=request.sid)
#
#     def on_leave_room(self, data):
#         sid = request.sid
#         gameid = str(data["game_id"])
#
#         room_name = '/' + gameid
#         leave_room(room_name)
#         print(sid + 'has left the room.')
#         game = Game.query.get_or_404(gameid)
#         payload = game.get_settings_to_json()
#         # emit(payload, to=room_name)
#
#     def on_game_loop(self, data):
#         # current user we do not know
#         gameid = str(data['game_id'])
#         room_name = '/' + gameid
#         phone = str(data['phone'])
#         g.current_payer = User.query.filter_by(phone=phone).first()
#         game = Game.query.get_or_404(gameid)
#
#         players_without_current = []
#         for player in game.players:
#             if player.id != g.current_user.id:
#                 players_without_current.append(player)
#
#         payload = {
#             "attempts": g.current_user.attempts,
#             "points": g.current_user.points,
#             "nick": g.current_user.nick,
#             "players": [player.player_to_json_game_update() for player in players_without_current]
#         }
#         print(payload)
#
#         emit('game_loop', payload, to=room_name)
#         # send(payload, to=request.sid)
#
#

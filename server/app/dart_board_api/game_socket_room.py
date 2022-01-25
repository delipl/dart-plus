from flask_socketio import send, Namespace, emit, join_room, leave_room
from flask import request


class GameSocketRoom(Namespace):


    def on_connect(self, data):
        print("connected with", request.sid)


    def on_game(self):
        pass

    def on_begin(self, data):
        sid = request.sid
        gameid = str(data["board_id"])
        room_name = "/game/" + gameid
        print("** JOIN ROOM **")
        print("Sid: ", sid)
        print("Board id to join: ", room_name)
        print("**           **")
        join_room(sid, room_name)
        respone = "Witam w pokoju: " + room_name
        add_new_room(room_name)
        # TEST
        print(socketio.server.manager.rooms["/"]["/game/1"])

        emit("game", respone, sid=sid)



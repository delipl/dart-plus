import time
from threading import Thread
from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit

from app.main.controller import infoController
from app.main.controller.gameController import delete_games
from app.main.database.database import create_tables
from app.main.service.gameService import gamePage
from app.main.service.infoService import infoPage, get_info
from app.main.service.userService import userPage
thread = None
app = Flask(__name__)
app.register_blueprint(userPage)
app.register_blueprint(infoPage)
app.register_blueprint(gamePage)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='threading')

# todo zeby nie napierdalac sprawdzaj czy sie cos zmienilo w danych
def background_thread():
    while True:
        time.sleep(0.06)
        socketio.emit('user_activated', infoController.get_info(1), broadcast=True)


@socketio.on('connect')
def connect():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()

@socketio.on('disconnect')
def disconnect():
    emit('retrieve_active_users')


# @socketio.on('activate_user')
# def on_active_user(data):
#     pass


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8000, debug=True)
    delete_games()
    socketio.run(app, debug=True, host='0.0.0.0', port=8000)

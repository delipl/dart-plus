import os
from flask_migrate import Migrate
import time
from threading import Thread
from flask_socketio import SocketIO, send, emit
from app import create_app, db
# do not remove any import !!!!
from app.models.user import User
from app.models.game import Game
from app.info import controller as infoController

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.app_context().push()
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


thread = None
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
    db.create_all()
    # Deleting games############
    games = Game.query.all()  #
    for game in games:         #
        db.session.delete(game)#
                               #
    db.session.commit()        #
    ############################
    socketio.run(app, debug=True, host='0.0.0.0', port=8000)
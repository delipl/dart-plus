import os
from flask_migrate import Migrate
import time
from threading import Thread
from flask_socketio import SocketIO, send, emit
from app import create_app, db
# do not remove any import !!!!
from app.models.user import User, user_game
from app.models.game import Game
from app.models.throw import Throw
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
    db.session.query(User).delete()
    db.session.query(Game).delete()
    db.session.commit()
    artur = User(name='Artur', phone='123456780', password='huj', nick='louda', wins='2137')
    bartek = User(name='Bartek', phone='123456789', password='huj', nick='la', wins='69')
    kuba = User(name='Kuba', phone='123456788', password='huj', nick='uda', wins='420')
    db.session.add(artur)
    db.session.add(bartek)
    db.session.add(kuba)
    db.session.commit()
    game = Game(startPoints='301')
    db.session.add(game)
    db.session.commit()

    artur.active_games.append(game)
    bartek.active_games.append(game)
    db.session.commit()

    # # Deleting games############
    # games = Game.query.all()   #
    # for game in games:         #
    #     db.session.delete(game)#
    #                            #
    # db.session.commit()        #
    # ############################
    socketio.run(app, debug=True, host='0.0.0.0', port=8000)

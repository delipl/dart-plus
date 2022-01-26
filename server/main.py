import os
from flask_migrate import Migrate
import time
from threading import Thread
from flask_socketio import SocketIO, send, emit
from app import create_app, db
# do not remove any import !!!!
from app.models.user import User, user_game
from app.models.game import Game
from app.models.dart_board import DartBoard
from app.models.throw import Throw
from app.dart_board_api.game_socket_esp import GameSocketEsp
from app.mobile_app_api.game_update_socket import GameSocketApp

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.app_context().push()
migrate = Migrate(app, db)
thread = None
socketio = SocketIO(app, cors_allowed_origins='*', logger=True, engineio_logger=True, ping_timeout=10, ping_interval=5)
socketio.on_namespace(GameSocketEsp('/esp'))
socketio.on_namespace(GameSocketApp('/app'))


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8000, debug=True)
    db.create_all()
    db.session.query(User).delete()
    db.session.query(Game).delete()
    db.session.query(DartBoard).delete()
    db.session.commit()
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

    # print(bartek.dart_board.id)

    # # Deleting games############
    # games = Game.query.all()   #
    # for game in games:         #
    #     db.session.delete(game)#
    #                            #
    # db.session.commit()        #
    # ############################
    socketio.run(app, debug=True, host='0.0.0.0', port=8000)

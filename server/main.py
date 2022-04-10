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


app, socketio = create_app(os.getenv('FLASK_CONFIG') or 'default')
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
    artur = User(name='Artur', phone='123456780', password='chuja', nick='louda',
                 wins='2137', board=dartBoard, attempts=0, points=301)
    bartek = User(name='Bartek', phone='123456789', password='chuja', nick='la', wins='69', board=dartBoard,
                  attempts=0, points=301)
    kuba = User(name='Kuba', phone='123456788', password='chuja', nick='uda', wins='420', board=dartboard2,
                attempts=0, points=301)
    ziom = User(name='ziom', phone='500100100', password='qwerty', nick='udaty', wins='420',
                attempts=0, points=301)
    db.session.add(ziom)
    db.session.add(artur)
    db.session.add(bartek)
    db.session.add(kuba)
    db.session.commit()
    game = Game(startPoints='301', throwingUserId=1, round=0, gameStatus=1)
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

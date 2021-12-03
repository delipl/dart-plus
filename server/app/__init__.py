from flask import Flask
from flask_cors import CORS

from app.main.database.database import create_tables
from app.main.service.gameService import gamePage
from app.main.service.infoService import infoPage
from app.main.service.userService import userPage

app = Flask(__name__)
app.register_blueprint(userPage)
app.register_blueprint(infoPage)
app.register_blueprint(gamePage)
CORS(app)


if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port=8000, debug=True)
from flask import Flask

app = Flask(__name__)

from app.main.service import userService

app.run(debug=True)

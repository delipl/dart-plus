from flask import Flask
from flask_cors import CORS

from app.main.database.database import create_tables

app = Flask(__name__)
CORS(app)
from app.main.service import userService

create_tables()
app.run(host='0.0.0.0', port=8000, debug=False)
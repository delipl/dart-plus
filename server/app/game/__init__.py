from flask import Blueprint

gamePage = Blueprint('gameService', __name__, template_folder='templates')

from . import service


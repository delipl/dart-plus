from flask import Blueprint

userPage = Blueprint('userService', __name__, template_folder='templates')

from . import service
from . import controller

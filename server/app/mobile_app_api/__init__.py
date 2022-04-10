from flask import Blueprint

mobileApp = Blueprint('mobileApp', __name__, template_folder='templates')

from . import service
from . import auth

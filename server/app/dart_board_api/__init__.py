from flask import Blueprint

dartBordApi = Blueprint('dartBordApi', __name__, template_folder='templates')

from . import service
from . import decorators


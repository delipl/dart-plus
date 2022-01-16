from flask import Blueprint

infoPage = Blueprint('infoService', __name__, template_folder='templates')

from . import service
from . import controller

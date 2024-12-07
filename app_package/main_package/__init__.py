from flask import Blueprint

bp = Blueprint('main', __name__)

from app_package.main_package import routes
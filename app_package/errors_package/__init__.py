from flask import Blueprint

bp = Blueprint('errors', __name__)

from app_package.errors_package import handlers
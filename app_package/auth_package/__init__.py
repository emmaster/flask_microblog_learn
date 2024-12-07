from flask import Blueprint

bp = Blueprint('auth', __name__)

from app_package.auth_package import routes
from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_babel import Babel

def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'uk_UA'

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

from app_package.errors_package import bp as errors_bp
app.register_blueprint(errors_bp)

login = LoginManager(app)
login.login_view = 'auth.login'
babel = Babel(app, locale_selector=get_locale)

from app_package.auth_package import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

from app_package.main_package import bp as main_bp
app.register_blueprint(main_bp, url_prefix='/main')


import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
import os

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='KLSNKVs blog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/klsnkv_blog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('KLSNKVs blog startup')


from app_package import models
from app_package.main_package import routes
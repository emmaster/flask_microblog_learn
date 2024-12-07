from flask import render_template
# from app_package import app, db
from app_package import db
from . import bp

# @app.errorhandler(404)
@bp.app_errorhandler(404) 
def not_found_error(error):
    return render_template('errors/404.html'), 404

# @app.errorhandler(500)
@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
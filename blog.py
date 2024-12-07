# from app_package import app, db
from app_package import db, create_app

# before we start we made this export FLASK_APP=blog.py
# now you can start an app just by typing in terminal flask run

import sqlalchemy as sa
import sqlalchemy.orm as so
from app_package.models import User, Post

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so':so, 'db': db, 'User': User, 'Post': Post}



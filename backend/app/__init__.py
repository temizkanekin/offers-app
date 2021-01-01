from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

# set up logging config
import logging
import os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

app = Flask(__name__)
Bootstrap(app)

from flask_sqlalchemy import SQLAlchemy

app.config['SECRET_KEY'] = 'E3H\xc2-\xe2-\xc3\xc7\xef\xf8\x90\x95\x1cDv'  # os.urandom(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
db.init_app(app)

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

from app.main import main as main_blueprint

app.register_blueprint(main_blueprint)

from app.auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)

from flask_login import LoginManager
from app.models import User, Product

login = LoginManager(app)
login.login_view = 'login'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

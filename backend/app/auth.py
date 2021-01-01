import logging

from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

from app.models import User

logger = logging.getLogger(__name__)

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('Login.html')


@auth.route('/logout')
@login_required
def logout():
    logger.info("User %s logged out", current_user.username)
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST'])
def login_post():
    form = request.form
    username = form['username']
    password = form['password']
    user = User.query.filter_by(username=username).first()
    if user is None or not check_password_hash(user.password, password):
        flash('Please check your login details and try again')
        return redirect(url_for('auth.login'))
    flash('Succesfully signed in.', 'positive')
    login_user(user)
    logger.info("User %s logged in", current_user.username)
    return redirect(url_for('main.home'))

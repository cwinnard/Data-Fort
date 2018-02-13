from flask import Blueprint, render_template, request, url_for
from flask_login import current_user

from .login_facilitator import LoginFacilitator
from psql.schema.master import User

loginBP = Blueprint('login', __name__, template_folder='templates', url_prefix='/login')

@loginBP.route('/')
def welcome():
    return render_template('login.html')

@loginBP.route('/<user_name>')
def log_user_in(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    LoginFacilitator().log_user_in(user)
    raise ValueError(str(current_user.id))
    return flask.url_for('dashboard')

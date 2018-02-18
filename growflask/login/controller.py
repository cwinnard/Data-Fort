from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user

from .login_facilitator import LoginFacilitator
from psql.schema.master import User

loginBP = Blueprint('login', __name__, template_folder='templates', url_prefix='/login')

@loginBP.route('/')
def welcome():
    return render_template('login.html')

@loginBP.route('/login-user')
def log_user_in():
    userName = request.args.get('username')
    user = User.query.filter_by(user_name=userName).first()
    LoginFacilitator().log_user_in(user)
    return redirect(url_for('dashboard.dashboard'))

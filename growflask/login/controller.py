from flask import Blueprint, current_user, render_template, request

loginBP = Blueprint('login', __name__, template_folder='templates', url_prefix='/login')

@loginBP.route('/')
def dashboard():
    return render_template('login.html')
from flask import Blueprint, render_template, request
#from flask_login import current_user

loginBP = Blueprint('login', __name__, template_folder='templates', url_prefix='/login')

@loginBP.route('/')
def dashboard():
    return render_template('login.html')
    
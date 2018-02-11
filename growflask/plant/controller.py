from flask import Blueprint, render_template, request
#from flask_login import current_user

from psql.schema.growing import Plant

plantBP = Blueprint('plant', __name__, template_folder='templates', url_prefix='/login')

@plantBP.route('/')
def dashboard():
    return 'hello plant'

@plantBP.route('/<int:plantId>/details')
def dashboard():
    return 'hello plant'

    
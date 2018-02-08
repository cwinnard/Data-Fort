from datetime import datetime
from flask import Blueprint, render_template, request

from growflask import db
from psql.schema.notebook import Reading

dashboardBP = Blueprint('dashboard', __name__, template_folder='templates', url_prefix='/dashboard')

@dashboardBP.route('/')
def dashboard():
    return 'hello dashboard'

@dashboardBP.route('/reading')
def reading():
	return render_template('reading.html')

@dashboardBP.route('/reading/add')
def take_reading():
    read_type = request.args.get('read_type')
    value = request.args.get('value')

    reading = Reading()
    reading.id_read_type = int(read_type)
    reading.value = value
    reading.id_taker = 1
    reading.id_plant = 1
    reading.date = datetime.now()

    db.session.add(reading)
    db.session.commit()

    return render_template('reading.html')
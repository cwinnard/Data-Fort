from datetime import datetime
from flask import Blueprint, jsonify, render_template, request
from flask_login import current_user

from growflask import db
from psql.schema.growing import Plant
from psql.schema.notebook import Reading

dashboardBP = Blueprint('dashboard', __name__, template_folder='templates', url_prefix='/dashboard')

@dashboardBP.route('/')
def dashboard():
    return render_template('dashboard.html')

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

@dashboardBP.route('/plants')
def plants():
    plants = Plant.query.filter_by(id_user=1).all()
    return render_template('plants.html', plants=plants)

@dashboardBP.route('/plants-json')
def plants_json():
    plants = Plant.query.filter_by(id_user=1).all()
    return jsonify(plants=[plant.serialize() for plant in plants])
from datetime import datetime
from flask import Blueprint, jsonify, render_template, request, url_for
from flask_login import current_user

from growflask import db
from psql.schema.growing import Plant
from psql.schema.notebook import Reading

dashboardBP = Blueprint('dashboard', __name__, template_folder='templates', url_prefix='/dashboard')

@dashboardBP.route('/')
def dashboard():
    return render_template('dashboard.html')

@dashboardBP.route('/plants')
def plants():
    plants = Plant.query.filter_by(id_user=1).all()
    return render_template('plants.html', plants=plants)

@dashboardBP.route('/plants-json')
def plants_json():
    plants = Plant.query.filter_by(id_user=1).all()
    return jsonify(plants=[plant.serialize() for plant in plants])
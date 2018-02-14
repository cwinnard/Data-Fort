from datetime import datetime
from flask import Blueprint, jsonify, redirect, render_template, request, url_for
#from flask_login import current_user

from growflask import db

from psql.schema.growing import Plant

plantBP = Blueprint('plant', __name__, template_folder='templates', url_prefix='/plant')

@plantBP.route('/')
def plant():
    return 'hello plant'

@plantBP.route('/add')
def add_plant():
    name = request.args.get('name')
    planted_on = request.args.get('planted_on')
    plant_date = datetime.strptime(planted_on, '%Y-%m-%dT%H:%M')

    plant = Plant()
    plant.id_user = 1
    plant.name = name
    plant.ts_start = plant_date

    db.session.add(plant)
    db.session.commit()

    return redirect(url_for('dashboard.plants'))   

@plantBP.route('/<int:plantId>/details')
def plant_details(plantId):
    plant = Plant.query.get(plantId)
    return render_template('plant-details.html', plant=plant)

@plantBP.route('/<int:plantId>/details-json')
def plants_details_json(plantId):
    plant = Plant.query.get(plantId)
    return jsonify(plant=plant.serialize())
 
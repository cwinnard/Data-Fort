from datetime import datetime
from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from growflask import db

from .plant_photo_manager import PlantPhotoManager
from psql.schema.growing import Plant
from psql.schema.notebook import Reading

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
    plant.id_user = current_user.id
    plant.name = name
    plant.ts_start = plant_date

    db.session.add(plant)
    db.session.commit()

    return redirect(url_for('dashboard.plants'))   

@plantBP.route('/<int:plantId>/details')
def details(plantId):
    plant = Plant.query.get(plantId)
    return render_template('plant-details.html', plant=plant)

@plantBP.route('/<int:plantId>/details-json')
def details_json(plantId):
    plant = Plant.query.get(plantId)
    return jsonify(plant=plant.serialize())

@plantBP.route('/<int:plantId>/readings/all-json')
def all_readings_json(plantId):
    readings = Reading.query.filter_by(id_plant=plantId).all()
    return jsonify(readings=[reading.serialize() for reading in readings])

@plantBP.route('/<int:plantId>/photo')
def get_photo(plantId):
    photoManager = PlantPhotoManager()
    photos = photoManager.get_photos(plantId)
    return None

@plantBP.route('/<int:plantId>/photo/add')
def add_photo(plantId):
    photoManager = PlantPhotoManager()
    photoManager.upload()
    return None

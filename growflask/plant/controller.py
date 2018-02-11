from flask import Blueprint, jsonify, render_template, request
#from flask_login import current_user

from psql.schema.growing import Plant

plantBP = Blueprint('plant', __name__, template_folder='templates', url_prefix='/plant')

@plantBP.route('/')
def plant():
    return 'hello plant'

@plantBP.route('/add')
def add_plant():
    return 'hello plant'    

@plantBP.route('/<int:plantId>/details')
def plant_details(plantId):
    plant = Plant.query.get(plantId)
    return render_template('plant_details.html', plant=plant)

@plantBP.route('/<int:plantId>/details-json')
def plants_details_json(plantId):
    plant = Plant.query.get(plantId)
    return jsonify(plant=plant.serialize())
 
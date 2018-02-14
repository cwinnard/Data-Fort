from datetime import datetime
from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from growflask import db
from psql.schema.growing import Plant
from psql.schema.notebook import Reading

notebookBP = Blueprint('notebook', __name__, template_folder='templates', url_prefix='/notebook')

@notebookBP.route('/reading')
def reading():
    return render_template('reading.html')

@notebookBP.route('/<int:plantId>/reading/add')
def take_reading(plantId):
    read_type = request.args.get('read_type')
    value = request.args.get('value')

    reading = Reading()
    reading.id_read_type = int(read_type)
    reading.value = value
    reading.id_taker = 1
    reading.id_plant = plantId
    reading.date = datetime.now()

    db.session.add(reading)
    db.session.commit()

    return redirect(url_for('plant.details', plantId=plantId))
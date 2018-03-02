from datetime import datetime
from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from growflask import db
from psql.schema.growing import Plant
from psql.schema.toolshed import Toolshed

dashboardBP = Blueprint('dashboard', __name__, template_folder='templates', url_prefix='/dashboard')

@dashboardBP.route('/')
def dashboard():
    return render_template('dashboard.html')

@dashboardBP.route('/<int:userId>/plants')
def plants(userId):
    plants = Plant.query.filter_by(id_user=userId).all()
    return render_template('plants.html', plants=plants)

@dashboardBP.route('/<int:userId>/plants-json')
def plants_json(userId):
    plants = Plant.query.filter_by(id_user=userId).all()
    return jsonify(plants=[plant.serialize() for plant in plants])

# NEED TO RESTIFY THESE ROUTES
@dashboardBP.route('/<int:userId>/toolsheds')
def toolshed(userId):
    toolsheds = Toolshed.query.all()
    #toolsheds = Toolshed.query.filter_by(id_user=userId).all()
    return render_template('toolsheds.html', toolsheds=toolsheds)

@dashboardBP.route('/<int:userId>/toolsheds-json')
def toolsheds_json():
    toolsheds = Toolshed.query.all()
    #toolsheds = Toolshed.query.filter_by(id_user=current_user.id).all()
    return jsonify(toolsheds=[toolshed.serialize() for toolshed in toolsheds])

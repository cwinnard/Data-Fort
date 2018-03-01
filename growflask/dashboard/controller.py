from datetime import datetime
from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from growflask import db
from psql.schema.growing import Plant
from psql.schema.notebook import Reading, ReadType
from psql.schema.toolshed import Tool, Toolshed

dashboardBP = Blueprint('dashboard', __name__, template_folder='templates', url_prefix='/dashboard')

@dashboardBP.route('/')
def dashboard():
    return render_template('dashboard.html')

@dashboardBP.route('/plants')
def plants():
    plants = Plant.query.filter_by(id_user=current_user.id).all()
    return render_template('plants.html', plants=plants)

@dashboardBP.route('/plants-json')
def plants_json():
    plants = Plant.query.filter_by(id_user=current_user.id).all()
    return jsonify(plants=[plant.serialize() for plant in plants])

# NEED TO RESTIFY THESE ROUTES
@dashboardBP.route('/toolshed')
def toolshed():
    toolsheds = Toolshed.query.all()
    #toolsheds = Toolshed.query.filter_by(id_user=current_user.id).all()
    return render_template('toolsheds.html', toolsheds=toolsheds)

@dashboardBP.route('/toolshed-json')
def toolsheds_json():
    toolsheds = Toolshed.query.all()
    #toolsheds = Toolshed.query.filter_by(id_user=current_user.id).all()
    return jsonify(toolsheds=[toolshed.serialize() for toolshed in toolsheds])

@dashboardBP.route('/toolshed/<int:toolshedId>/add-tool')
def toolshed_add_tool(toolshedId):
    name = request.args.get('name')
    read_type_id = request.args.get('read_type')

    toolshed = Toolshed.query.get(toolshedId)
    read_type = ReadType.query.get(read_type_id)

    tool = Tool()
    tool.name = name
    tool.read_type = read_type
    tool.toolsheds_in += [toolshed]

    db.session.add(tool)
    db.session.commit()

    return redirect(url_for('dashboard.toolshed')) 
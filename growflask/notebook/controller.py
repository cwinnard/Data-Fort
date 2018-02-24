from datetime import datetime
from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from growflask import db
from psql.schema.growing import Plant
from psql.schema.notebook import Reading, ReadType, ReadTypeCategory

notebookBP = Blueprint('notebook', __name__, template_folder='templates', url_prefix='/notebook')

@notebookBP.route('/reading')
def reading():
    return render_template('reading.html')

@notebookBP.route('/<int:plantId>/reading/add')
def take_reading(plantId):
    read_type = request.args.get('read_type')
    value = request.args.get('value')
    tool = request.args.get('tool')

    reading = Reading()
    reading.id_read_type = int(read_type)
    reading.value = value
    reading.id_taker = current_user.id
    reading.id_plant = plantId
    reading.ts_reading_taken = datetime.now()
    reading.id_tool = tool

    db.session.add(reading)
    db.session.commit()

    return redirect(url_for('plant.details', plantId=plantId))

#Admin routes
@notebookBP.route('/admin/read-types')
def admin_read_types():
    read_types = ReadType.query.all()
    return render_template('admin-read-types.html', read_types=read_types)

@notebookBP.route('/admin/read-types/add')
def add_read_type():
    name = request.args.get('name')
    description = request.args.get('description')
    category = request.args.get('category')
    target_value = request.args.get('target_value')
    frequency = request.args.get('frequency')

    read_type = ReadType()
    read_type.name = name
    read_type.description = description
    read_type.id_read_type_category = category
    read_type.target_value = target_value
    read_type.frequency = frequency

    db.session.add(read_type)
    db.session.commit()

    return redirect(url_for('notebook.admin_read_types'))

@notebookBP.route('/admin/read-type-categories')
def admin_read_type_categories():
    categories = ReadTypeCategory.query.all()
    return render_template('admin-read-type-categories.html', categories=categories)

@notebookBP.route('/admin/read-type-categories/add')
def add_read_type_category():
    name = request.args.get('name')
    description = request.args.get('description')
    color = request.args.get('color')

    category = ReadTypeCategory()
    category.name = name
    category.description = description
    category.color = color

    db.session.add(category)
    db.session.commit()

    return redirect(url_for('notebook.admin_read_type_categories'))
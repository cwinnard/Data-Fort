from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from growflask import db
from psql.schema.toolshed import Toolshed

toolshedBP = Blueprint('toolshed', __name__, template_folder='templates', url_prefix='/toolshed')

@toolshedBP.route('/<int:toolshedId>')
def toolshed(toolshedId):
    toolshed = Toolshed.query.get(toolshedId)
    return render_template('toolshed.html', toolshed=toolshed)
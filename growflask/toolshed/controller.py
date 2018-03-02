from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from growflask import db
from psql.schema.notebook import ReadType
from psql.schema.toolshed import Tool, Toolshed

toolshedBP = Blueprint('toolshed', __name__, template_folder='templates', url_prefix='/toolshed')

@toolshedBP.route('/<int:toolshedId>')
def toolshed(toolshedId):
    toolshed = Toolshed.query.get(toolshedId)
    return render_template('toolshed.html', toolshed=toolshed)

@toolshedBP.route('/<int:toolshedId>/add-tool')
def add_tool(toolshedId):
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

    return redirect(url_for('toolshed.toolshed', toolshedId=toolshedId)) 
from growflask import db

from .tool import Tool
from .toolshed import Toolshed

metadata = db.Metadata(schema='toolshed')

toolshed_tool = db.Table('toolshed_tool', metadata, \
    db.Column('id_toolshed', db.Integer, db.ForeignKey(ToolShed.id), nullable=False), \
    db.Column('id_tool', db.Integer, db.ForeignKey(Tool.id), nullable=False)
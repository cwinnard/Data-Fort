from growflask import db


class ToolshedTool(db.Model):
    """Junction table between tool and toolshed """

    __table_args__ = {'schema': 'toolshed'}
    __tablename__ = 'toolshed_tool'

    id = db.Column(db.Integer, primary_key=True)
    id_tool = db.Column(db.Integer, db.ForeignKey('toolshed.tool.id'), primary_key=True)
    id_toolshed = db.Column(db.String(128), db.ForeignKey('toolshed.toolshed.id'), primary_key=True)
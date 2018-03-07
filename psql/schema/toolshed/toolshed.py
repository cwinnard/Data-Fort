from growflask import db
from psql.schema.master import Operation
from .team_toolshed import TeamToolshed
from .toolshed_tool import ToolshedTool


class Toolshed(db.Model):
    """Represents a collection of tools"""

    __table_args__ = {'schema': 'toolshed'}
    __tablename__ = 'toolshed'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    id_operation = db.Column(db.Integer, db.ForeignKey(Operation.id), nullable=True)

    tools = db.relationship('Tool', secondary=ToolshedTool.__table__)
    teams = db.relationship('Team', secondary=TeamToolshed.__table__)

    def serialize(self):
        return {
            'name': self.name, 
            'tools': [tool.serialize() for tool in self.tools],
            'operation': self.operation.name if self.operation else None
        }
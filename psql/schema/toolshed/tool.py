from growflask import db

from .toolshed_tool import toolshed_tool


class Tool(db.Model):
    """Represents a tool used to take a reading on a plant """

    __table_args__ = {'schema': 'toolshed'}
    __tablename__ = 'tool'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    #Importing read_type as string instead of model to avoid circular import
    id_read_type = db.Column(db.Integer, db.ForeignKey('notebook.read_type.id'), nullable=False)

    read_type = db.relationship('ReadType', lazy='joined')
    toolsheds_in = db.relationship('Toolshed', secondary=toolshed_tool, lazy='subquery', back_populates='toolsheds_in')

    def serialize(self):
        return {
            'name': self.name, 
            'read_type': self.read_type.name
        }
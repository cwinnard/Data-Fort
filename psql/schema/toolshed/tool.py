from growflask import db


class Tool(db.Model):
    """Represents a tool used to take a reading on a plant """

    __table_args__ = {'schema': 'toolshed'}
    __tablename__ = 'tool'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    #Importing read_type as string instead of model to avoid circular import
    id_read_type = db.Column(db.Integer, db.ForeignKey('read_type.id'), nullable=False)

    read_type = db.relationship('ReadType', lazy='joined')
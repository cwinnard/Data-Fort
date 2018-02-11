from growflask import db

class ReadType(db.Model):
    """Represents the types of readings that can be taken """

    __table_args__ = {'schema': 'notebook'}
    __tablename__ = 'read_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
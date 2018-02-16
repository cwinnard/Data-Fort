from growflask import db


class ReadTypeCategory(db.Model):
    """Represents an entry in the notebook """

    __table_args__ = {'schema': 'notebook'}
    __tablename__ = 'read_type_category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=True)
    color = db.Column(db.String(128), nullable=True)

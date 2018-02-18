from growflask import db
from .operation import Operation


class Team(db.Model):
    """Represents a person"""

    __table_args__ = {'schema': 'master'}
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    id_operation = db.Column(db.Integer, db.ForeignKey(Operation.id), nullable=True)
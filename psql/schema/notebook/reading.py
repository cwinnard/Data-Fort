from growflask import db

from psql.schema.growing import Plant
from psql.schema.master import User
from .read_type import ReadType


class Reading(db.Model):
    """Represents an entry in the notebook """

    __table_args__ = {'schema': 'notebook'}
    __tablename__ = 'reading'

    id = db.Column(db.Integer, primary_key=True)
    id_plant = db.Column(db.Integer, db.ForeignKey(Plant.id), nullable=False)
    ts_reading_taken = db.Column(db.DateTime(), nullable=False)
    id_read_type = db.Column(db.Integer, db.ForeignKey(ReadType.id), nullable=False)
    value = db.Column(db.String(128), nullable=False)
    id_taker = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    read_type = db.relationship('ReadType', lazy='joined')

    @property
    def color(self):
        return self.read_type.color

    def serialize(self):
        return {
            'read_type': self.read_type.name, 
            'value': self.value,
            'ts_reading_taken': self.ts_reading_taken,
            'color': self.color,
        }
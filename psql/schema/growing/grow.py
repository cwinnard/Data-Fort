from flask import jsonify
from time import strftime

from growflask import db


class Grow(db.Model):
    """Represents a collection of plants"""

    __table_args__ = {'schema': 'growing'}
    __tablename__ = 'grow'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    ts_start = db.Column(db.DateTime(), nullable=False)
    ts_end = db.Column(db.DateTime())
    phase = db.Column(db.String(128))

    @property
    def plant_date(self):
        return self.ts_start.strftime('%b %d %Y')

    @property
    def recent_readings(self):
        from psql.schema.notebook import Reading
        return Reading.query.filter_by(id_plant=self.id).order_by(db.desc(Reading.ts_reading_taken)).limit(5).all()

    def serialize(self):
        return {
            'name': self.name, 
            'planted_on': self.plant_date,
            'recent_readings': [reading.serialize() for reading in self.recent_readings]
        }
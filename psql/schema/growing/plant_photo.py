from flask import jsonify
from time import strftime

from growflask import db

from psql.schema.master import User


class PlantPhoto(db.Model):
    """Represents information about a photo uploaded for a plant"""

    __table_args__ = {'schema': 'growing'}
    __tablename__ = 'plant_photo'

    id = db.Column(db.Integer, primary_key=True)
    id_plant = db.Column(db.Integer, db.ForeignKey('psql.schema.plant.id'), nullable=False)
    ts_uploaded = db.Column(db.DateTime(), nullable=False)
    notes = db.Column(db.String(128))
    ts_deleted = db.Column(db.DateTime())

    plant = db.relationship('Plant', backref='photos')
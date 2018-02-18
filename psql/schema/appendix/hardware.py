from growflask import db

from psql.schema.master import User


class Lighting(db.Model):
    """Represents a plant"""

    __table_args__ = {'schema': 'appendix'}
    __tablename__ = 'lighting'

    id = db.Column(db.Integer, primary_key=True)
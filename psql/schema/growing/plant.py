from growflask import db

from psql.schema.master import User


class Plant(db.Model):
    """Represents a plant"""

    __tablename__ = 'plant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    ts_start = db.Column(db.DateTime(), nullable=False)
    ts_end = db.Column(db.DateTime())
    id_user = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
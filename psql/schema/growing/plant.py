from time import strftime

from growflask import db

from psql.schema.master import User


class Plant(db.Model):
    """Represents a plant"""

    __table_args__ = {'schema': 'growing'}
    __tablename__ = 'plant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    ts_start = db.Column(db.DateTime(), nullable=False)
    ts_end = db.Column(db.DateTime())
    id_user = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    @property
    def plant_date(self):
        return self.ts_start.strftime('%b %d %Y')

    def serialize(self):
        return {
            'name': self.name, 
            'owner': self.user.user_name,
            'planted_on': self.plant_date,
        }
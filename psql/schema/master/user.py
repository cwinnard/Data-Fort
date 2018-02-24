from growflask import db

from .operation import Operation
from .team import Team
from psql.schema.toolshed import Toolshed


class User(db.Model):
    """Represents a person"""

    __table_args__ = {'schema': 'master'}
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(128), nullable=False)
    name_first = db.Column(db.String(128), nullable=False)
    name_last = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    #id_operation = db.Column(db.Integer, db.ForeignKey(Operation.id), nullable=True)
    #id_team = db.Column(db.Integer, db.ForeignKey(Team.id), nullable=True)
    #id_toolshed = db.Column(db.Integer, db.ForeignKey(Toolshed.id), nullable=True)

    plants = db.relationship('Plant', backref='user', lazy='joined')

    #????Needs to return unicode rather than int per flask login????
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
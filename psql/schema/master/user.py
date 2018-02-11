from growflask import db


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

    plants = db.relationship('Plant', backref='user', lazy='joined')
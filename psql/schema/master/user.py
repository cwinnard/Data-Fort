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
    authenticated = db.Column(db.Boolean, default=False)

    plants = db.relationship('Plant', backref='user', lazy='joined')

    #Needs to return unicode rather than int per flask login
    def get_id(self):
        return char(self.id)

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
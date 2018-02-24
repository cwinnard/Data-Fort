from growflask import db


class UserOperaion(db.Model):
    """Junction table between user and operation"""

    __table_args__ = {'schema': 'master'}
    __tablename__ = 'user_operation'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('master.user.id'), primary_key=True)
    id_operation = db.Column(db.Integer, db.ForeignKey('master.operation.id'), primary_key=True)
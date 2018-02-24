from growflask import db


class OperationTeam(db.Model):
    """Junction table between operation and team """

    __table_args__ = {'schema': 'master'}
    __tablename__ = 'operation_team'

    id = db.Column(db.Integer, primary_key=True)
    id_operation = db.Column(db.Integer, db.ForeignKey('master.operation.id'), primary_key=True)
    id_team = db.Column(db.Integer, db.ForeignKey('master.team.id'), primary_key=True)
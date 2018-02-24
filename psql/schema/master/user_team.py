from growflask import db


class UserTeam(db.Model):
    """Junction table between user and team """

    __table_args__ = {'schema': 'master'}
    __tablename__ = 'user_team'

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('master.user.id'), primary_key=True)
    id_team = db.Column(db.Integer, db.ForeignKey('master.team.id'), primary_key=True)
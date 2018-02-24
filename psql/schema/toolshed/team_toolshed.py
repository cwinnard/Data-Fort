from growflask import db


class TeamToolshed(db.Model):
    """Junction table between team and toolshed """

    __table_args__ = {'schema': 'toolshed'}
    __tablename__ = 'team_toolshed'

    id = db.Column(db.Integer, primary_key=True)
    id_team = db.Column(db.Integer, db.ForeignKey('master.team.id'), primary_key=True)
    id_toolshed = db.Column(db.Integer, db.ForeignKey('toolshed.toolshed.id'), primary_key=True)
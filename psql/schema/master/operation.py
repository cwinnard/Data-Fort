from growflask import db


class Operation(db.Model):
    """Represents a person"""

    __table_args__ = {'schema': 'master'}
    __tablename__ = 'operation'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    teams = db.relationship('Team', backref='operation')
    toolsheds = db.relationship('Toolshed', backref='operation')

    def serialize(self):
    return {
        'name': self.name, 
        'teamNames': [team.name for team in self.teams],
        'toolshedNames': [toolshed.name for toolshed in self.toolsheds]
    }
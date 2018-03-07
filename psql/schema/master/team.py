from growflask import db

from psql.schema.toolshed.team_toolshed import TeamToolshed


class Team(db.Model):
    """Represents a person"""

    __table_args__ = {'schema': 'master'}
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    id_operation = db.Column(db.Integer, db.ForeignKey('master.operation.id'), nullable=True)

    members = db.relationship('Team', secondary='master.user_team')
    toolsheds = db.relationship('Toolshed', secondary=TeamToolshed.__table__)

    def serialize(self):
        return {
            'name': self.name, 
            'owner': self.operation.name,
            'members': [user.serialize() for user in self.members]
        }
from growflask import db


class Team(db.Model):
    """Represents a person"""

    __table_args__ = {'schema': 'master'}
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    id_operation = db.Column(db.Integer, db.ForeignKey('master.operation.id'), nullable=True)

    members = db.relationship('Team', secondary='master.user_team')

    def serialize(self):
        return {
            'name': self.name, 
            'owner': self.operation.name,
            'members': [user.serialize() for user in self.members]
        }
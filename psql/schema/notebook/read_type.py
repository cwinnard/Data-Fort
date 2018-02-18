from growflask import db

from .read_type_category import ReadTypeCategory


class ReadType(db.Model):
    """Represents the types of readings that can be taken """

    __table_args__ = {'schema': 'notebook'}
    __tablename__ = 'read_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    id_read_type_category = db.Column(db.Integer, db.ForeignKey(ReadTypeCategory.id), nullable=True)

    category = db.relationship('ReadTypeCategory', lazy='joined')

    @property
    def color(self):
    	return self.category.color if self.category else 'transparent'

    def serialize(self):
        return {
            'name': self.name, 
            'description': self.description,
            'color': self.color,
        }
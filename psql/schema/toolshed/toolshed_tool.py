from growflask import db

metadata = db.MetaData(schema='toolshed')

toolshed_tool = db.Table('toolshed_tool', metadata, \
    db.Column('id_toolshed', db.Integer, db.ForeignKey('toolshed.id'), primary_key=True, nullable=False), \
    db.Column('id_tool', db.Integer, db.ForeignKey('tool.id'), primary_key=True, nullable=False))
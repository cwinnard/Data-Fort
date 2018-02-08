from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)

app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

from growflask.dashboard.controller import dashboardBP
app.register_blueprint(dashboardBP)

@app.route('/')
def index():
	return 'hello application'
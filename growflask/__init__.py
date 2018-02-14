from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager

import config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

#Need work on login
"""
loginManager = login_manager.LoginManager()

from psql.schema.master import User
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

loginManager.init_app(app)
"""
from growflask.dashboard.controller import dashboardBP
app.register_blueprint(dashboardBP)
from growflask.login.controller import loginBP
app.register_blueprint(loginBP)
from growflask.notebook.controller import notebookBP
app.register_blueprint(notebookBP)
from growflask.plant.controller import plantBP
app.register_blueprint(plantBP)

@app.route('/')
def index():
	return 'hello application'

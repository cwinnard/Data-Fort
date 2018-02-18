from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager

import config

# Create clask app
app = Flask(__name__)
app.secret_key = 'STAND42.334526BY-83.045908'

#Configure db connection
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

#Configure login
loginManager = login_manager.LoginManager()
from psql.schema.master import User
@loginManager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
loginManager.init_app(app)

#Configure blueprints
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
	return redirect(url_for('login.welcome'))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#Why isnt this working?!
#from flask_login import LoginManager

import config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


from growflask.dashboard.controller import dashboardBP
app.register_blueprint(dashboardBP)
from growflask.login.controller import loginBP
app.register_blueprint(loginBP)
from growflask.plant.controller import plantBP
app.register_blueprint(plantBP)

@app.route('/')
def index():
	return 'hello application'

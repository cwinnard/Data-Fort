from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
from test_data import Facilities
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, IntegerField, StringField, TextAreaField, PasswordField, validators

fitfort = Flask(__name__)

# Config and initialize db
fitfort.config['SQLALCHEMY_DATABASE_URI ']= 'postgresql://JStemp12:Swingline5!@localhost/fitfort'
db = SQLAlchemy(fitfort)

Facilities = Facilities()

class User(db.Model):
    __tablename__= 'user'

    user_id = db.Column(db.Integer, unique=True, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    f_name = db.Column(db.String(50))
    l_name = db.Column(db.String(50))
    sex = db.Column(db.String(50))
    bdate = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, user_id, username, password, f_name, l_name, sex, bdate, email):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.f_name = f_name
        self.l_name = l_name
        self.sex = sex
        self.bdate = bdate
        self.email = email

"""
#class Facility(db.Model):
class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(JSON)
    result_no_stop_words = db.Column(JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)
"""
@fitfort.route('/')
def home():
    user=User.query.all()
    return render_template('home.html', user=user)

@fitfort.route('/users')
def users():
    # select * from user
    return render_template('users.html')

@fitfort.route('/facilities')
def facilities():
    # select * from facility
    return render_template('facilities.html', facilities = Facilities)

@fitfort.route('/facility/<int:fac_id>/')
def facility(fac_id):
    # select * from facility
    return render_template('facility.html',fac_id=fac_id)

@fitfort.route('/workouts')
def workouts():
    # select * from workout
    return render_template('workouts.html')

@fitfort.route('/sets')
def sets():
    # select * from set
    return render_template('sets.html')

@fitfort.route('/exercises')
def exercises():
    # select * from exercises
    return render_template('exercises.html')

@fitfort.route('/equipment_list')
def equipment_list():
    # select * from equipment
    return render_template('equipment_list.html')

"""
@fitfort.route('/new_user/<user_id>')
def new_user():
    return render_template('new_user.html')
"""
@fitfort.route('/reset_pw')
def reset_pw():
    return render_template('reset_pw.html')
"""
@fitfort.route('/user/<user_id>')
def user():
    return render_template('user.html')

@fitfort.route('/dashboard/<user_id>')
def dashboard():
    return render_template('dashboard.html')

@fitfort.route('/')
def hello():
    return render_template('home.html')
"""
class RegisterForm(Form):
    user_id = IntegerField('User ID', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=1, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
        ])
    confirm =PasswordField('Confirm Password')
    f_name = StringField('First Name', [validators.Length(min=1, max=50)])
    l_name = StringField('Last Name', [validators.Length(min=1, max=50)])
    sex = StringField('Sex', [validators.Length(min=1, max=50)])
    bdate = StringField('Date of Birth (YYYY-MM-YY)', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=1, max=50)])
"""
@fitfort.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user_id = form.user_id.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        f_name = form.f_name.data
        l_name = form.l_name.data
        sex = form.sex.data
        bdate = form.bdate.data
        email = form.email.data

    return render_template('register.html', form=form)
"""
@fitfort.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and form.validate():
        user=User()
        db.session.add(user)
        return('Success')




if __name__ == '__main__':
    fitfort.run(debug=True)

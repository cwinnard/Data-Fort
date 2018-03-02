from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import current_user

from growflask import db

dashboardBP = Blueprint('toolshed', __name__, template_folder='templates', url_prefix='/toolshed')

@dashboardBP.route('/')
def toolshed():
    return render_template('toolshed.html')
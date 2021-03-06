"""
Main Flask application object
"""
from flask import (Flask, abort, request, redirect, Response, make_response,
                   session, url_for)
from flask import render_template
from flaskext.csrf import csrf
import jinja2
from jinja2 import evalcontextfilter, Markup, escape

from db import db
import settings, users, views
from mongsession import MongoSessionInterface

app = Flask(__name__)
app.debug = True
app.session_interface = MongoSessionInterface(db)
app.register_blueprint(views.blue)
app.register_blueprint(users.views)
users.setup(app, users.OFUser)
csrf(app)

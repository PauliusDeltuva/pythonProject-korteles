import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from korteles import app


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, '../database/cards.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()

from korteles.models import *
from korteles import routes

# def create_app():
#   app = Flask(__name__)
#   app.config['DEBUG'] = True
#   db.init_app(app)
#   return app
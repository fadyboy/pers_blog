# application initiation file

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# use environment application settings variable from config file

app.config.from_object(os.environ['APP_SETTINGS'])

# create instance of database object
db = SQLAlchemy(app)

from app import views, models
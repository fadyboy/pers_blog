# application initiation file

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# use application settings from config file
app.config.from_object('config')

# create instance of database object
db = SQLAlchemy(app)

from app import views, models
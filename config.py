# config file settings for application

import os

# set base directory file path to a variable
basedir = os.path.abspath(os.path.dirname(__file__))

# specify database connection string
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'bdd_app.db')

CSRF_ENABLED = True
SECRET_KEY = 'very-secret'
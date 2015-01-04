# config file settings for application

import os

basedir = os.path.abspath(os.path.dirname(__file__))
#
class BaseConfig(object):

    DEBUG = True
    SECRET_KEY = 'KY\xfa\xc0\x80/|\xad\x98\xe5\x14\xb2\xbb~4'
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):

    DEBUG = True
    # specify path for local development database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'bdd_app.db')


class ProductionConfig(BaseConfig):

    DEBUG = False
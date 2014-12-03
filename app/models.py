# database models for application

from app import db
import urllib # to use special methods to format urls

# define class models for the Category and Interests

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, db.Sequence('category_id'), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name

    # create class method to format category name as url
    # @classmethod
    # def format_name(cls, category_name):
    #     name = urllib.unquote(category_name)
    #
    #     return db.session.query(cls.name == name)
    #
    # # create general method to remove white space from url
    # def format_url(self):
    #     escaped_name = self.name
    #     return "/{}".format(escaped_name)

    # add a relationship to the Interests table
    category_interests = db.relationship('Interests', backref = 'category', lazy = 'dynamic')

    def __repr__(self):
        return '{}'.format(self.name)


class Interests(db.Model):
    __tablename__ = 'interests'

    id = db.Column(db.Integer, db.Sequence('interest_id'), primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id')) #remove _id from category

    def __init__(self, title, url, category_id):
        self.title = title
        self.url = url
        self.category_id = category_id

    def __repr__(self):
        return '{}'.format(self.title)


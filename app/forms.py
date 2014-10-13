# forms for the application
from flask.ext.wtf import Form
from wtforms import TextField, SelectField
from models import Category
from app import db


# create Interest form class to add categories for the interests

class CategoryForm(Form):
    category = TextField('category')

# create Interest form class to add details of the actual interests to categories

class InterestForm(Form):
    # create list of categories by querying db
    categories = db.session.query(Category).all()
    title = TextField('title')
    url = TextField('url')
    category = SelectField('category', choices=[(choice.id, choice.name) for choice in categories])

    # def set_category_choices(self):
    #     self.category.choices = db.session.query(Category).all()
    #     return self.category.choices



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
    title = TextField('title')
    url = TextField('url')
    category = SelectField('category', choices=[])

    # create method to refresh list of categories when instance of form created

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.refresh()

    def refresh(self):
        self.category.choices = [(unicode(choice.id), choice.name) for choice in db.session.query(Category).all()]



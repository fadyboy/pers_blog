# forms for the application
from flask.ext.wtf import Form
from wtforms import TextField, SelectField


# create Interest form class to add categories for the interests

class CategoryForm(Form):
    category = TextField('category')

# create Interest form class to add details of the actual interests to categories

class InterestForm(Form):
    title = TextField('title')
    url = TextField('url')
    category = SelectField('category')

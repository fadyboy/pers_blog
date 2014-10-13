# views for application

from app import app
from app import db
from flask import render_template, request
from forms import CategoryForm, InterestForm
from models import Category, Interests
from sqlalchemy.exc import IntegrityError
import urllib


# add functions to create urls for the Category pages
def encode_url(category_name):
    '''
        Function to replace white spaces from string passed as category name with underscore
        or escaped characters
    '''
    #return category_name.replace(' ', '_')
    return urllib.quote(category_name)

def decode_url(category_name_url):
    '''
        Function to replace underscore or escaped characters with white space
    '''
    #return category_name_url.replace('_', ' ')
    return urllib.unquote(category_name_url)

@app.route('/')
@app.route('/home')
def home():
    # query database for list categories list and display last 5 added
    category_list = db.session.query(Category).all()

    for category in category_list:
        category.url = encode_url(category.name)

    return render_template('home.html', title='Home', category=category_list)

@app.route('/about')
def about():

    return render_template('about.html', title='About')

# view to add a new interest category
@app.route('/interests', methods=['GET','POST'])
def interests():
    # create new instance of Category form
    form = CategoryForm(request.form)
    message = ""

    if form.validate_on_submit():
        new_category = Category(form.category.data)

        # catch database integrity exception if duplicate category added
        try:
            db.session.add(new_category)
            db.session.commit()
            message = "{} category added".format(new_category)
        except IntegrityError:
            message = "Category already exists!"
    # create an empty instance of form if no form submitted
    else:
        form = CategoryForm()


    return render_template('interests.html', title='Interests', form=form, message=message)

# create view for Category interest page
@app.route('/<path:category_name>')
def category_name(category_name):
    category = decode_url(category_name)

    return render_template('category.html', category=category)

# view to add and interest page to an interest category
@app.route('/add_page', methods=['GET', 'POST'])
def add_page():
    # get all categories in database
    # categories = db.session.query(Category).all()
    # create an instance of the page interests form
    form = InterestForm(request.form)
    #form.category.choices = form.set_category_choices()
    #form.category.choices = [(choice.id, choice.name) for choice in categories]
    # form.set_category_choices()
    message = ""

    if form.validate_on_submit():
        interest_page = Interests(form.title.data, form.url.data, form.category.data)
        db.session.add(interest_page)
        db.session.commit()
        message = "{} interest page added".format(interest_page)

    else:
        form = InterestForm()


    return render_template('add_page.html', form=form, message=message)
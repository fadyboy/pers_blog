# views for application

from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html', title='Home')

@app.route('/about')
def about():

    return render_template('about.html', title='About')

@app.route('/interests')
def interests():

    return render_template('interests.html', title='Interests')
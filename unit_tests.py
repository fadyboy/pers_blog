# unit tests for bdd_app

import unittest
from app import app, db
from config import basedir
import os
from app.models import Category, Interests
from sqlalchemy.exc import IntegrityError


class AppTests(unittest.TestCase):

    # setup for unit tests
    def setUp(self):
        app.config['Testing'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, 'test_db.db')
        self.app = app.test_client() # create client test browser

        db.create_all()

    # teardown for unit tests
    def tearDown(self):
        db.session.remove()
        db.drop_all()


    # create test to add new interest category
    def add_category_test(self):
        new_category = Category('jammo')
        db.session.add(new_category)
        db.session.commit()
        test = db.session.query(Category).first()

        self.assertEqual('jammo', test.name)

    # create test to check for duplicate interest category
    def duplicate_category_test(self):
        first_category = Category('first_name')
        db.session.add(first_category)
        db.session.commit()

        # add another category with the same name
        # wrap in a method that is called in assertRaises
        def duplicate_entry():
            second_category = Category('first_name')
            db.session.add(second_category)
            db.session.commit()

        #self.assertRaises(IntegrityError, db.session.commit(), db.session.add(second_category))
        self.assertRaises(IntegrityError, duplicate_entry)

    # create test to add interest pages to categories
    def add_interest_page_test(self):
        pass

    # create test to display interest page details in interest category page
    def display_interest_in_category_page_test(self):
        pass


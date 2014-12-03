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
        interest_page = Interests("test_title", "http://test.com", 3)
        db.session.add(interest_page)
        db.session.commit()

        # check title and url exist in category
        self.assertEqual("test_title", interest_page.title)
        self.assertEqual("http://test.com", interest_page.url)

    # create test to display list of interest page details for interest category page
    # the list is based on the interest category
    def display_interest_in_category_page_test(self):
        # create category
        current_category = Category('Test_category')
        other_category =Category('Other_category')

        # add and commit databases to db
        db.session.add_all([current_category, other_category])
        db.session.commit()

        current_category_id = current_category.id
        other_category_id = other_category.id

        # add interest page
        interest1 = Interests("Test", "http://test.com", current_category_id)
        interest2 = Interests("Test2", "http://test2.com", current_category_id)
        interest3 = Interests("Test3", "http://test3.com",other_category_id)

        # add and commit interests to database
        db.session.add_all([interest1, interest2, interest3])
        db.session.commit()

        # return interest pages details based on current category
        pages = db.session.query(Interests).filter(Interests.category_id == current_category_id)
        # verify that all pages have the same category id
        for page in pages:
            self.assertEqual(current_category_id, page.category_id)

        # verify that pages do not belong to other category
        for page in pages:
            self.assertNotEqual(other_category_id, page.category_id)

    def no_interests_in_category_test(self):
        # create category
        current_category = Category("Test_category")
        db.session.add(current_category)
        db.session.commit()

        interest = Interests("Test", "http://test.com", 1)

        # check that there are no interest pages in category and that list is empty
        pages = db.session.query(Interests).filter(Interests.category_id == 1).all()
        self.assertEqual([], pages)
# Environment parameters

import logging
from selenium import webdriver

# run before each test
def before_all(context):
    context.selenium_logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
    context.selenium_logger.setLevel(logging.WARN)
    context.browser = webdriver.Firefox()
    # context.response = context.browser.get('http://localhost:5000')

# run after each test
def after_all(context):
    context.browser.quit()
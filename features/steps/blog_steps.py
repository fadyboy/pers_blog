# test steps for the blog feature
#from behave import *

# step for scenario navigate to the blog home page
@Given(u'that I have a web browser open')
def step_impl(context):
    pass

@When(u'I type in the url for the blog website and press enter')
def step_impl(context):
    # launch browser and go to home page
    # context.response
    br = context.browser
    br.get('http://localhost:5000')

@Then(u'I am taken to the homepage for the blog website')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000')
    assert "Home" in br.title

# step for scenario to navigate to the About Me page
@Given(u'that I on the Home page')
def step_impl(context):
    context.browser.get('http://localhost:5000')

@When(u'I click the About page hyperlink')
def step_impl(context):
    br = context.browser
    about_link = br.find_element_by_link_text('About Me')
    about_link.click()


@Then(u'I am taken to the About page')
def step_impl(context):
    br = context.browser
    assert "About" in br.title

# steps for scenario to navigate to the Add interests page
@Given(u'Given that I am on the Home page')
def step_impl(context):
    #context.browser.get('http://localhost:5000')
    br = context.browser
    br.get('http://localhost:5000')


@When(u'When I click the Add Interests hyperlink')
def step_impl(context):
    br = context.browser
    add_interest_link = br.find_element_by_link_text('Add Interests')
    add_interest_link.click()

@Then(u'')
def step_impl(context):
    br = context.browser
    assert "Interest" in br.title

# scenario to add an interest category that displays on homepage
@Given(u'that I am on the add interest page')
def step_impl(context):
    br = context.browser
    br.get('http://localhost:5000/interests')

@When(u'I add a new interest category in the category text field and click the submit button')
def step_impl(context):
    pass

@Then(u'the new category is added and listed in the homepage')
def step_impl(context):
    pass



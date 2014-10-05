# test steps for the blog feature

# step for scenario navigate to the blog home page
@When(u'I type in the url for the blog website and press enter')
def step_impl(context):
    # launch browser and go to home page
    # context.response
    br = context.browser
    br.get('http://localhost:5000')

@Then(u'I am taken to the homepage for the blog website')
def step_impl(context):
    br = context.browser
    br.gt('http://localhost:5000')
    assert br.title == 'Personal Blog'

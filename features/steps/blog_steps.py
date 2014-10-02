# test steps for the blog feature

# step for scenario navigate to the blog home page
@When(u'I type in the url for the blog website and press enter')
def step_impl(context):
    # launch browser and go to home page
    context.response

@Then(u'I am taken to the homepage for the blog website')
def step_impl(context):
    context.response
    assert context.response.title == 'Personal Blog'

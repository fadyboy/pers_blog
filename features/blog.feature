Feature: Confirming that Blog homepage, About page, and Special Interest page display when navigated to

    Scenario: The blog home page is displayed when first navigated to the website
        Given that I have a web browser open
        When I type in the url for the blog website and press enter
        Then I am taken to the homepage for the blog website


    Scenario: The About page is displayed when navigated to
        Given that I on the Home page
        When I click the About page hyperlink
        Then I am taken to the About page

    Scenario: The Add Interests page is displayed when navigated to
        Given that I am on the Home page
        When I click the Add Interests hyperlink
        Then I am taken to the Add Interests page

    Scenario: An interest category is added and displayed on the homepage when I add a new interest category
        Given that I am on the add interest page
        When I add a new interest category in the category text field and click the submit button
        Then the new category is added and listed in the homepage



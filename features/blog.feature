Feature: Confirming that Blog homepage, About page, and Special Interest page display when navigated to

    Scenario: The blog home page is displayed when first navigated to the website
        Given that I have a web browser open
        When I type in the url for the blog website and press enter
        Then I am taken to the homepage for the blog website


    Scenario: The About page is displayed when navigated to
        Given that I on the Home page
        When I click the About page hyperlink
        Then I am taken to the About page

    Scenario: The Special Interests page is displayed when navigated to
        Given that I am on the Home page
        When I click the Special Interests hyperlink
        Then I am taken to the Special Interests page

    Scenario: The question to vote for is displayed on the homepage
        Given that I am on the homepage for the blog site
        Then I will see the question for the day

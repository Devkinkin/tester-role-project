Feature: Login behaviour

  Scenario: Valid login succeeds
    Given I open the demo login page
    When I enter valid credentials
    Then I should reach the secure area

  Scenario: Invalid password is rejected
    Given I open the demo login page
    When I enter a valid username and an invalid password
    Then I should see an invalid password message

  Scenario: Empty credentials are rejected
    Given I open the demo login page
    When I submit empty credentials
    Then I should remain unauthenticated

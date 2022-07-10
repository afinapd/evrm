Feature: Pokemon Flow

  Scenario: User can access website pokemon
    Given launch chrome browser
    When user open evermos page
    And user go to sign in page
    And user login with no HP "6281223334444" and password "password"
    Then user successfully login to the homepage
    And close browser
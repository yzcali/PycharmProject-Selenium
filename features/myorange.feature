Feature: OrangeHRM logo
  Scenario: Logo presence on OrangeHRM home Page
    Given launch chrome browser
    When open orange hrm homepage
    Then verify that the logo present on page
    And close browser

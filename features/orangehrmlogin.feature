Feature: OrangeHRM login
  Scenario: Login to OrangeHRM with valid parameters
    Given I launch Chrome browser
    When I open orange HRM homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard page


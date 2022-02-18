Feature: HW3 BDD Part2
  A BDD for user to check if cart is empty

  Scenario: User can check if cart is empty
    Given Open Amazon Home Page
    When Click cart button
    Then Verify if empty cart message

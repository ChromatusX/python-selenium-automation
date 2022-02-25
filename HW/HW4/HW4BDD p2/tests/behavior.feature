# Created by hongl at 2/24/2022
Feature:  Adding product to cart
  Checks if user is able to successfully add item to cart

  Scenario: User adds a game to cart
    Given Open Amazon page
    When Input board games on search bar
    Then Click the search button
    Then Click on first item to add
    Then Add item to cart
    Then Verify item in cart
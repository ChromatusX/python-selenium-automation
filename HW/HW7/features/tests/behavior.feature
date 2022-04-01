# Created by hongl at 3/31/2022
Feature: Page Object Pattern Scenarios
  # Enter feature description here

  Scenario: Check for sign in page on Amazon
        Given Open Amazon home page
        When Click on returns and orders
        Then Verify Sign-In page

  Scenario: User can check if cart is empty
        Given Open Amazon Home Page
        When Click cart button
        Then Verify Your Amazon Cart is empty text present
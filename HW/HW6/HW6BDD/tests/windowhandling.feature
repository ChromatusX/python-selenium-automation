# Created by hongl at 3/12/2022
Feature: Window handling case with amazon T&C
  # Enter feature description here

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original window
    Then Click on Amazon Privacy Notice link
    When Switch to new window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window and switch back to original

# Created by hongl at 2/17/2022
Feature: HW3 BDD Part1
  A BDD for user to search information on canceling an order in the help page

  Scenario: User can search for canceling an order on help page
    Given Open Amazon help page
    When Search for Cancel order
    Then Verify if help page
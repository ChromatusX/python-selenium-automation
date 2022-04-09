# Created by hongl at 4/8/2022
Feature: HW8
  # Enter feature description here

    Scenario: searching in different department on Amazon
        Given Open Amazon home page
        When Select books department
        And Search for Game
        Then Verify books department is selected

    Scenario: Verify new Arrivals
        Given Open item page
        When Hover over arrival
        Then Verify new arrival details
Feature: CRUD features for tickets on Trello board
  As a Trello user,
  I want to be able to create, read, update and delete tickets on Trello board
  So that I can efficiently organise my day to day work


  Background:
    Given that Im logged in to Trello


  Scenario: Check that user is able to create cards on Trello board
    When I go to the board
    And create card
    Then newly created card is shown on the Trello board


  Scenario: Check that user can update card on Trello board
    When I go to the board
    And create card
    When update card
    Then changes will be shown in the card


  Scenario: Check that user can delete card from the Trello board
    When I go to the board
    And create card
    And I archive card and I delete archived card
    Then deleted card wont be shown on the Trello board
Feature: busqueda de empleo
  Background:
    Given the user is on "https://www.alten.es/#empleo"
    And the user accepts the terms and conditions if they do not exist

  Scenario: Job search with position term "Programador"
    Given the user writes "Programador" in the position or search term field
    Then the table should display job offers that match the search term:"Programador"

  Scenario: Job search with city "madrid"
    Given the user writes "madrid" in the city or postal code field
    Then the table should display job offers that match the search city:"madrid"

  Scenario: Job search with position term "PHP" and city "madrid"
    Given the user writes "PHP" in the position or search term field
    And the user writes "madrid" in the city or postal code field
    Then the table should display job offers that match the search "PHP" and "madrid"

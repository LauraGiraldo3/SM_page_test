Feature: Contact-us form
  As a user
  I want to fill out the contact-us form
  In order to contact Source Meridian team

  Background: Go to contact-us form page
    Given the user open the Source Meridian home page
    Given the user clicks on menu options
    Given the user clicks on 'Contact us' option

  Scenario: Fill out the contact-us form successfully
    When the user fills out all the fields correctly
    Then a success message is displayed

  Scenario: Fill out name field with invalid data
    When the user fills out name field with invalid data
    Then an error message is displayed

  Scenario: Fill out email field with invalid data
    When the user fills out email field with invalid data
    Then an error message is displayed

  Scenario: Fill out company field with invalid data
    When the user fills out company field with invalid data
    Then an error message is displayed

  Scenario: Fill out message field with invalid data
    When the user fills out message field with invalid data
    Then an error message is displayed

  Scenario: Do not check the terms and conditions checkbox
    When the user do not check the terms and conditions checkbox
    Then an error message is displayed
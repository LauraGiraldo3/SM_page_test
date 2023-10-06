Feature: Contact-us form
  As a user
  I want to fill out the contact-us form
  In order to contact Source Meridian team

  Background: Go to contact-us form page
    Given the user open the Source Meridian home page
    Given the user clicks on menu options
    Given the user clicks on 'Contact us' option

  @correct_form
  Scenario: Fill out the contact-us form successfully
    When the user fills out all the fields correctly
    Then a success message is displayed

  @invalid_data
  Scenario Outline: Fill out fields with invalid data
    When the user fills out '<field_name>' with '<invalid_data>'
    Then general error message is displayed
    Then field error message is displayed
    Examples:
    | field_name | invalid_data |
    | name       | 1234%$       |
    | name       | empty        |
    | email      | laura        |
    | email      | empty        |
    | company    | 43@%?        |
    | company    | empty        |
    | number     | laura        |
    | number     | empty        |
    | message    | 45$#%        |
    | message    | empty        |

  @dont_check_terms
  Scenario: Do not check the terms and conditions checkbox
    When the user do not check the terms and conditions checkbox
    Then general error message is displayed
    Then field error message is displayed
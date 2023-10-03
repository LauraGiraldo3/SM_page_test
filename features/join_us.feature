Feature: Join us section
  As a user
  I want to go to 'Join us' section
  In order to apply to a job

  Background: Search QA Automation job
    Given the user open the Source Meridian home page
    Given the user clicks on 'Join us' option
    Given the user select 'QA Automation' job

  Scenario: Fill out the form to apply to QA Automation job
    When the user clicks on Apply Now button
    Then the user can fill out the form
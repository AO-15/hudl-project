
Feature: Login to Hudl
    As a Hudl User
    I want to log in to the website
    So that I can have access to Hudl

    Background:
        Given I am on the Login Page

    Scenario: Successful login with valid credentials
        When I enter valid login credentials
        And I click the Log In button
        Then I should be redirected to the Home Page

    Scenario: Login with invalid credentials
        When I enter invalid login credentials
        And I click the Log In button
        Then I should see an error message
        And The Log In button should be disabled

    Scenario: Login with an organization
        When I click the Login with an organization button
        Then I should see the login with an organization page


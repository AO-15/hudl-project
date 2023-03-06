
# test_login.py
from pytest_bdd import scenarios, given, when, then, parsers
import pytest

from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.credentials import coach_account as valid_user, invalid_coach_account as invalid_user


scenarios("../features/login_page.feature")


@given("I am on the Login Page")
def go_to_login_page(login_page):
    login_page.go_to_login_page()

@when("I enter valid login credentials")
def enter_valid_credentials(login_page):
    login_page.enter_credentials(valid_user.get("username"), valid_user.get("password"))

@when("I enter invalid login credentials")
def enter_invalid_credentials(login_page):
    login_page.enter_credentials(invalid_user.get("username"), invalid_user.get("password"))

@when("I click the Log In button")
def click_login_button(login_page):
    login_page.click_login_button()

@when("I click the Login with an organization button")
def click_login_with_org(login_page):
    login_page.click_login_with_org()

@then("I should be redirected to the Home Page")
def redirected_to_home_page(login_page):
    login_page.wait_for_title("Home - Hudl")
    assert login_page.get_current_url() == HomePage.HOME_PAGE_URL

@then("I should see an error message")
def is_error_message_displayed(login_page):
    assert login_page.is_error_message_displayed()

@then("The Log In button should be disabled")
def is_login_button_disabled(login_page):
    assert login_page.is_login_button_disabled()

@then("I should see the login with an organization page")
def login_with_org(login_page):
    login_page.wait_for_title("Log In with Organization - Hudl")
    assert login_page.get_current_url() == LoginPage.LOGIN_WITH_ORG_URL

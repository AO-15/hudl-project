
import time
from utils.selenium_base import DriverFactory, SeleniumBase
from locators.locators import LoginLocators

class LoginPage(SeleniumBase):
    LOGIN_PAGE_URL = "https://www.hudl.com/login"
    LOGIN_WITH_ORG_URL = "https://www.hudl.com/app/auth/login/organization"


    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        """
        Navigates to the login page.
        """
        self.driver.get(self.LOGIN_PAGE_URL)

    def enter_credentials(self, email: str, password: str):
        """
        Enter the login email and password credentials.
        """
        self.wait_for_visible_element(LoginLocators.EMAIL_INPUT)
        self.wait_for_visible_element(LoginLocators.PASSWORD_INPUT)
        self.send_keys(LoginLocators.EMAIL_INPUT, email)
        self.send_keys(LoginLocators.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """
        Click login button.
        """
        self.click(LoginLocators.LOGIN_BUTTON)

    def login(self, email: str, password: str):
        """
        Login with the given email and password credentials and Click Login button.
        """
        self.enter_credentials(email, password)
        self.click_login_button


    def is_error_message_displayed(self) -> bool:
        """
        Checks if an error message is displayed.
        """
        try:
            error_display = self.wait_for_visible_element(LoginLocators.ERROR_DISPLAY)
            return error_display.is_displayed()
        except:
            return False
        
    def is_login_button_disabled(self) -> bool:
        """
        Checks if login button is disabled
        """
        btn = self.find_element(LoginLocators.LOGIN_BUTTON)
        is_disabled = not btn.is_enabled()
        return is_disabled
    
    def get_home_page_title(self) -> str:
        """
        Waits and gets the page title for Home Page
        """
        self.wait_for_title("Home - Hudl")
        return self.driver.title

    def click_login_with_org(self) -> None:
        """
        Clicks the Login with Org button
        """
        self.click(LoginLocators.LOGIN_WITH_ORG_BTN)
    

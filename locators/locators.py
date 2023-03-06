from selenium.webdriver.common.by import By

class HomePageLocators:
    LOGIN_IN_BUTTON = (By.XPATH, "//a[normalize-space()='Log in']")

class LoginLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#logIn")
    ERROR_DISPLAY = (By.CSS_SELECTOR, "p[data-qa-id='error-display']")
    LOGIN_WITH_ORG_BTN = (By.CSS_SELECTOR, "button[data-qa-id='log-in-with-organization-btn']")

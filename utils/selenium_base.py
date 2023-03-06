from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver


class SeleniumBase:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    def find_element(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def wait_for_visible_element(self, locator: tuple, timeout: int = 10) -> WebElement:
        """
        Wait for an element to be visible on the page.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} not visible after {timeout} seconds")

    def wait_for_clickable_element(self, locator: tuple, timeout: int = 10) -> WebElement:
        """
        Wait for an element to be clickable on the page.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} not clickable after {timeout} seconds")

    def wait_for_title(self, title: str, timeout: int = 10) -> None:
        """
        Wait for the page title to match the specified title.
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.title_is(title)
            )
        except TimeoutException:
            raise AssertionError(f"Page title not '{title}' after {timeout} seconds")

    def click(self, locator: tuple) -> None:
        """
        Find an element and click it.
        """
        element = self.wait_for_clickable_element(locator)
        element.click()

    def click_ele(self, element: WebElement) -> None:
        """
        Click an Element
        """
        element.click()

    def send_keys(self, locator: tuple, text: str) -> None:
        """
        Find an element and enter text into it.
        """
        element = self.wait_for_visible_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """
        Find an element and return its text.
        """
        element = self.wait_for_visible_element(locator)
        return element.text

    def is_element_visible(self, locator: tuple) -> bool:
        """
        Check if an element is visible on the page.
        """
        try:
            self.wait_for_visible_element(locator, timeout=1)
            return True
        except AssertionError:
            return False
        
    def find_and_scroll(self, locator: tuple):
        """
        Find Element then scroll into view.
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        
    def wait_and_scroll(self, locator: tuple, timeout: int = 10):
        """
        Waits for visible element then scrolls into view
        
        """
        element = self.wait_for_visible_element((locator), timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_current_url(self):
        return self.driver.current_url

class DriverFactory:
    @staticmethod
    def create_driver(browser: str) -> webdriver:
        """
        Create a new instance of the specified browser driver.
        """
        if browser == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--window-size=1920,1080")
            driver = Chrome(options=chrome_options)
        elif browser == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--window-size=1920,1080")
            driver = Firefox(options=firefox_options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        return driver

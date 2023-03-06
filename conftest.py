
import pytest
from pages.login_page import LoginPage
from utils.selenium_base import DriverFactory
from settings import BROWSER

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=BROWSER, help="Type in browser name e.g. chrome OR firefox")

@pytest.fixture
def login_page(browser):
    driver = DriverFactory.create_driver(browser)
    return LoginPage(driver)


def pytest_sessionstart(session):
    session.results = dict()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    driver = DriverFactory.create_driver(BROWSER)
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            screenshot = driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, "Screenshot"))
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            
        report.extra = extra

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")
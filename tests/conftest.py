from selenium import webdriver
from base.webdriverfactor import WebDriverFactor
from pages.home.login_page import LoginPage
import pytest

#Function level
@pytest.fixture()
def setUp():
    print("Running method level setup")
    yield
    print("Running method level tear down")

#Module level
@pytest.fixture(scope="class")
def ModulesetUp(request, browser, osType):
    print("Running module level setup")
    wdf = WebDriverFactor(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("test@email.com","abcabc")
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running module level tear down")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType",help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
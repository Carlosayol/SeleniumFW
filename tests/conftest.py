from selenium import webdriver
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
    if browser=="chrome":
        baseUrl = "https://courses.letskodeit.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        print("Running test on Chrome")
    else:
        print("Running test on Mew")
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
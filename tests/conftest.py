import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome"),
    parser.addoption("--username", action="store", default="ananya.dutta0303@gmail.com"),

    parser.addoption(
        "--password", action="store", default="abcd@1234"
    )


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-error')
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service(r"C:/PythonProjects/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "Firefox":
        print("firefox driver")
        service_obj = Service(r"C:\Users\Nat\Downloads\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    else:
        service_obj = Service(r"C:/PythonProjects/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()


@pytest.fixture(scope="class")
def get_username(request):
    username = request.config.getoption("username")
    print(username)
    return username


@pytest.fixture(scope="class")
def get_password(request):
    password = request.config.getoption("password")
    print(password)
    return password

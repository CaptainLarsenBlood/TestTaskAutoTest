import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    print("\nstart browser for test..")
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Remote(
    command_executor='http://192.168.1.124:4444',
    options=chrome_options
)
    yield browser
    print("\nquit browser..")
    browser.quit()
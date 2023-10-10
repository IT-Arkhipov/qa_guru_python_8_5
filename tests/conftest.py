import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.driver.maximize_window()
    browser.config.timeout = 2.0

    browser.config.base_url = "https://demoqa.com"

    yield

    browser.quit()

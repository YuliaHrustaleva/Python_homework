import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def shop_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def calc_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Generator


@pytest.fixture(scope="function")
def shop_driver() -> Generator[WebDriver, None, None]:
    """Фикстура для инициализации и закрытия браузера Firefox"""
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def calc_driver() -> Generator[WebDriver, None, None]:
    """Фикстура для инициализации и закрытия браузера Chrome"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

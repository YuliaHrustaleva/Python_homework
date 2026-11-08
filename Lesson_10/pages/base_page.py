from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """Инициализация базовой страницы
        с драйвером и явными ожиданиями"""
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element_clickable(
            self, locator: Tuple[str, str]
            ) -> WebElement:
        """Ожидает когда элемент станет кликабельным
         и возвращает его"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator: Tuple[str, str]) -> WebElement:
        """Ожидает когда элемент отобразится в DOOM-дереве
         и возвращает его"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_text_in_element(
            self, locator: Tuple[str, str], text: str
            ) -> bool:
        """Ожидает появление нужного текста внутри элемента.
        Возвращает True или False """
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

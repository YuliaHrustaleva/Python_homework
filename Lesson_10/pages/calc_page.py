from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from typing import List, Tuple


class CalcPage(BasePage):
    """Класс для описания и взаимодействия со страницей калькулятора.
    Наследуется от основного класса BasePage"""
    DELAY_INPUT: Tuple[str, str] = (By.ID, "delay")
    SCREEN: Tuple[str, str] = (By.CSS_SELECTOR, ".screen")

    @staticmethod
    @allure.step("Формируем локатор для кнопки '{text}'")
    def button_locator(text: str) -> Tuple[str, str]:
        """Формирует и возвращает кортеж-локатор (By.XPATH, ...)
         для кнопки с текстом."""
        return By.XPATH, f"//span[text()='{text}']"

    def set_delay(self, seconds: int) -> None:
        """Устанавливает задержку в секундах"""
        el = self.wait_for_presence(self.DELAY_INPUT)
        el.clear()
        el.send_keys(str(seconds))

    def press_buttons(self, sequence: List[str]) -> None:
        """Последовательно нажимает кнопки калькулятора"""
        for text in sequence:
            btn = self.wait_for_element_clickable(
                  self.button_locator(text))
            btn.click()

    def wait_result(
            self, expected_text: str, timeout: int = 60
            ) -> None:
        """Ожидает появление нужного текста на экране калькулятора
         в течении установленного таймера """
        self.wait = WebDriverWait(self.driver, timeout)
        self.wait_for_text_in_element(self.SCREEN, expected_text)

    def get_result(self) -> str:
        """Получает текущий текст,
        отображаемый на экране калькулятора """
        return self.wait_for_presence(self.SCREEN).text

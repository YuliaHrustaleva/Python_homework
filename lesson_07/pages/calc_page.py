from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lesson_07.pages.base_page import BasePage

class CalcPage(BasePage):
    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    @staticmethod
    def button_locator(text):
        return (By.XPATH, f"//span[text()='{text}']")

    def set_delay(self, seconds):
        el = self.wait_for_presence(self.DELAY_INPUT)
        el.clear()
        el.send_keys(str(seconds))

    def press_buttons(self, sequence):
        for text in sequence:
            btn = self.wait_for_element_clickable(self.button_locator(text))
            btn.click()

    def wait_result(self, expected_text, timeout=60):
        self.wait = WebDriverWait(self.driver, timeout)
        self.wait_for_text_in_element(self.SCREEN, expected_text)

    def get_result(self):
        return self.wait_for_presence(self.SCREEN).text
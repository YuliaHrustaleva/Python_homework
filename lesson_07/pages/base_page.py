from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_text_in_element(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

#Тест 1. Ожидание появления динамического контента
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_controls():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    #Нажмите кнопку Remove.
    remove_btn = driver.find_element(By.XPATH, "//button[text()='Remove']")
    remove_btn.click()

   #Дождитесь появления текста It's gone! проверить, что текст появился
    message = wait.until(
        EC.text_to_be_present_in_element((By.ID, "message"), "It's gone!")
    )
    message_element = driver.find_element(By.ID, "message")
    assert message_element.text == "It's gone!", "Сообщение 'It's gone!' не появилось"

    #Нажмите кнопку Enable.
    enable_btn = driver.find_element(By.XPATH, "//button[text()='Enable']")
    enable_btn.click()

    #Дождитесь, когда поле ввода станет активным.
    input_field = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
    )
    assert input_field.is_enabled(), "Поле ввода не стало активным"

    #Проверьте, что поле действительно стало активным.
    input_field.send_keys("Hello World")
    assert input_field.get_attribute("value") == "Hello World", "Текст не ввелся в поле"

    driver.quit()
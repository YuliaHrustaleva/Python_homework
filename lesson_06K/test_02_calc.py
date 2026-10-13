from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_calculate():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # ждем появления поля ввода и вводим 45
    input_delay = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "delay")))
    input_delay.clear()
    input_delay.send_keys("45")

    #нажимаем на кнопки 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # задаем таймер 46 секунд и ждем появления значения 15
    wait = WebDriverWait(driver, 46)
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    # проверка, что значение 15 появилось через 45 минут
    assert driver.find_element(By.CSS_SELECTOR, ".screen").text == "15"

    driver.quit()











from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Найдите и нажмите на кнопку Start.
    start_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']"))
    )
    driver.execute_script("arguments[0].click();", start_btn)


    # # Дождитесь появления текста Hello World!
    finish_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='finish']/h4"))
    )

    driver.save_screenshot("screenshots/finish.png")

    # Проверьте, что появившийся текст равен Hello World!
    assert finish_element.text == "Hello World!", "Сообщение 'Hello World!' не появилось"

    driver.quit()



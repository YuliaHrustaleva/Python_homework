from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_loading_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # заполняем все поля, кроме Zip code
    driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")

    driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")

    driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")

    driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")

    driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")

    driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")

    driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")

    driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")

    driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")


    # нажимаем на кнопку submit
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # ждем, что первое поле станет зеленым
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element_attribute((By.ID, "first-name"), "class", "alert-success")
    )

    # проверка, что поле Zip code подсвечено красным
    zip_container = driver.find_element(By.ID, "zip-code")
    zip_classes = zip_container.get_attribute("class")
    assert "alert-danger" in zip_classes, f"Поле Zip code не подсвечено красным! Классы: {zip_classes}"

    # Проверка, что остальные поля подсвечены зеленым
    green_input_fields = [
        "first-name", "last-name", "address", "city",
        "country", "e-mail", "phone", "job-position", "company"
    ]

    for field_id in green_input_fields:
        container = driver.find_element(By.ID, field_id)
        container_classes = container.get_attribute("class")
        assert "alert-success" in container_classes, f"Поле {field_id} не подсвечено зеленым! Классы: {container_classes}"

    driver.quit()

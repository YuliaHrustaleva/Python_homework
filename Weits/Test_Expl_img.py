# ИСПОЛЬЗОВАНИЕ ЯВНЫХ ОЖИДАНИЙ
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# проверка, что для каждой картинки соответствует правильная ссылка на нее

def test2_image_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )

    #список картинок
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    assert len(images) == 4

    expected_files = [
        "compass.png",
        "calendar.png",
        "award.png",
        "landscape.png"
    ]

    for i, img in enumerate(images):
        src = img.get_attribute("src")
        assert expected_files[i] in src
        assert img.is_displayed()

    driver.quit()
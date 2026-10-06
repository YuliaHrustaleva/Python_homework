# ИСПОЛЬЗОВАНИЕ НЕЯВНЫХ ОЖИДАНИЙ

from selenium import webdriver
from selenium.webdriver.common.by import By


#проверка, что для каждой картинки соответствует правильная ссылка на нее

def test_image_loading():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


    #Ждем появления каждого изображения по их id
    compass_image = driver.find_element(By.ID, "compass")
    calendar_image = driver.find_element(By.ID, "calendar")
    award_image = driver.find_element(By.ID, "award")
    landscape_image = driver.find_element(By.ID, "landscape")

    #список картинок
    images = [compass_image, calendar_image, award_image, landscape_image]

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

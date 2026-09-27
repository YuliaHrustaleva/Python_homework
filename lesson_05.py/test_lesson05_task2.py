from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_submit():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    sleep(2)

    driver.find_element(By.NAME, "custname").send_keys("Юлия")

    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    sleep(2)

    assert driver.current_url == "https://httpbin.qa-territory.online/post"
    sleep(2)

    driver.quit()





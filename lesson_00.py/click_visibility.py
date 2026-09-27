from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/visibility")

button_hide = driver.find_element(By.ID, "hideButton")
button_hide.click()

button_visibility_hidden = driver.find_element(By.ID, "invisibleButton")

if button_visibility_hidden.is_displayed():
    print("кнопка видна")

else:
    print("кнопка скрыта")

driver.quit()


from re import search
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://gitflic.ru")
driver.find_element(By.CLASS_NAME, "cookiesBtn").click() # нажимаем на принять куки

sleep(3)
# клик на кнопку "начать работу", поиск по классу

click_button = driver.find_element(By.CLASS_NAME, "button-start")
click_button.click()
sleep(3)

# вводим логин и пароль
input_login = driver.find_element(By.ID, "email")
input_login.send_keys("in6vq@airsworld.net")

input_password = driver.find_element(By.ID, "passwordBasic")
input_password.send_keys("12345Qwerty")

#sleep(3)
#input_login.clear()
#input_password.clear()

# нажимаем на кнопку Войти
submit_button = driver.find_element(By.CLASS_NAME, "btn-success")
submit_button.click()

sleep(3)

user_name = driver.find_element(By.CLASS_NAME, "profile-page__profile-name")
print(user_name.text)

search_input = driver.find_element(By.CSS_SELECTOR, "input.gf-custom-search__input")
print(search_input.get_attribute("placeholder"))

driver.quit()

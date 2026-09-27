import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)

driver.get("https://www.google.com")

print(driver.title) # выведет title страницы
print(driver.current_url) #выведет url страницы
driver.refresh() # обновит страницу

time.sleep(2)

driver.quit()



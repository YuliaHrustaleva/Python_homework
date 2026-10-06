from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://gitflic.ru/")


# Добавляем cookie с токеном авторизации
driver.add_cookie({
   "name": "SESSION",
   "value": "MGM2NzQ5ZjQtYTY0NC00NjNmLTgyNWEtMzgwYWFiYWRlM2U0",
   "domain": "gitflic.ru"
})
# Добавляем cookie для окна подтверждения работы с cookie
driver.add_cookie({
   "name": "cookiesAccepted",
   "value": "true",
   "domain": "gitflic.ru"
})

# Обновляем страницу, чтобы cookie применилась
driver.refresh()


# Теперь мы авторизованы!
# Можем сразу перейти в личный кабинет
driver.get("https://gitflic.ru/user/ydikusar")
sleep(2)

# Удаляем все cookies (выходим из аккаунта)
driver.delete_all_cookies()


# Обновляем страницу
driver.refresh()
sleep(2)

driver.quit()








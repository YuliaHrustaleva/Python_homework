from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_yougile_login():
    driver = webdriver.Chrome()
    # Открыть страницу авторизации: https://ru.yougile.com/team/
    driver.get("https://ru.yougile.com/team/")
    driver.maximize_window()
    sleep(3)

    #Ввести в поле «Email» логин: jil-jj@yandex.ru "[autocomplete='email']"
    driver.find_element(By.CSS_SELECTOR, "[autocomplete='email']").send_keys(
        "jil-jj@yandex.ru"
    )
    sleep(2)

    #Ввести в поле «Пароль» пароль: Alena-1322  [autocomplete="current-password"]
    driver.find_element(By.CSS_SELECTOR, "[autocomplete='current-password']").send_keys("Alena-1322")
    sleep(2)

    #Нажать кнопку «Войти»   .bg-action-default[role="button"]
    driver.find_element(By.CSS_SELECTOR, ".bg-action-default[role='button']").click()
    sleep(5)

    driver.get("https://ru.yougile.com/team/settings-account")
    sleep(5)


    user_name = driver.find_element(By.CSS_SELECTOR, "[placeholder='Отображаемое имя…']")

    assert user_name.is_displayed()
    assert user_name.get_attribute("value") == "Юлия"

    driver.quit()



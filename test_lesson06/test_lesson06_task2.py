from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    driver.get("https://gitflic.ru/")

    #установить куки user1
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

    # Перейти на страницу профиля.
    driver.get("https://gitflic.ru/user/ydikusar")

    # Обновляем страницу, чтобы cookie применилась
    driver.refresh()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".user-profile__username")))

    # сохранить текущий url
    url_user1 = driver.current_url
    print(f"url user1: {url_user1}")

    #очистить куки user1 и обновить страницу
    driver.delete_all_cookies()
    driver.refresh()

    # установить куки user2
    driver.add_cookie({
        "name": "SESSION",
        "value": "Yzc4OWE5MmMtYjk1Ny00ZDM3LTg5NzQtNjc3NTYyMzMxZmFk",
        "domain": "gitflic.ru"
    })
    # Добавляем cookie для окна подтверждения работы с cookie
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    # Перейти на страницу профиля user2.
    driver.get("https://gitflic.ru/user/airsworld")

    # Обновляем страницу, чтобы cookie применилась
    driver.refresh()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".user-profile__username")))

    # сохранить текущий url
    url_user2 = driver.current_url
    print(f"url user2: {url_user2}")

    # проверяем, что url_user1 и url_user2 различаются
    assert url_user1 != url_user2, f"Ошибка! URL одинаковые: {url_user1}"
    print("URL пользователей различаются!")

    driver.delete_all_cookies()
    driver.refresh()

    driver.quit()



import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
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

    yield driver
    driver.quit()
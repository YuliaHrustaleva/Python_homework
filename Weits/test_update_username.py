from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def test_update_username(driver):
    wait = WebDriverWait(driver, 10)
    #Перейти на страницу профиля.
    driver.get("https://gitflic.ru/user/ydikusar")

    driver.save_screenshot("screenshots/full_screen.png")

    #Нажать кнопку редактирования профиля.
    edit_button = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "user-profile__edit")
    ))
    edit_button.click()

    #Изменить фамилию и имя в форме.
    username_input = wait.until(EC.presence_of_element_located(
        (By.ID, "name")
    ))
    username_input.clear()
    username_input.send_keys("Юлия")

    surname_input = wait.until(EC.presence_of_element_located(
        (By.ID, "surname")
    ))
    surname_input.clear()
    surname_input.send_keys("Хрусталева")

    #Сохранить изменения.
    save_button = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".gf-button.--success")
    ))
    save_button.click()

    #Вернуться на страницу профиля.
    driver.get("https://gitflic.ru/user/ydikusar")

    driver.save_screenshot("screenshots/full_screen_after.png")

    #Ожидаемый результат: фамилия и имя успешно изменены и отображаются на странице профиля.
    user_name = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "h6.mb-0")
    ))
    user_name.screenshot("screenshots/user_name.png")

    assert user_name.text == "Юлия Хрусталева"

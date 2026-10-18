from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shopping():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)


    # Авторизуйтесь как пользователь  standard_user и нажимаем на кнопку login
    wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(
        EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()


    # ищем нужный товар и добавляем в корзину
    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()

    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    # Проверка, что на элементе "корзина" появилась цифра 3
    wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "3"))
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "3"

    # переходим в корзину
    wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

    # Нажмите Checkout.
    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Заполните форму своими данными: имя, фамилия, почтовый индекс.
    wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Юлия")
    wait.until(
        EC.presence_of_element_located((By.ID, "last-name"))).send_keys("Хрусталева")
    wait.until(
        EC.presence_of_element_located((By.ID, "postal-code"))).send_keys("142506")

    # Нажмите кнопку Continue.
    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    # ждем элемент с итоговой стоимостью (Total).
    total_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
    total_text = total_element.text

    # Проверка, что итоговая сумма равна $58.29
    assert "Total: $58.29" in total_text, f"Ожидалась сумма $58.29, но на странице отображается: {total_text}"

    # нажимаем на кнопку finish
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    # проверка, что попали на страницу успешного завершения заказа
    assert wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))).is_displayed()

    driver.quit()

from pages.shop_page import ShopPage
import allure


@allure.feature("Оформление заказа в онлайн-магазине")
@allure.title("Успешное оформление заказа")
@allure.description("Тест проверяет")
def test_shopping(shop_driver):

    with allure.step("Открыть страницу онлайн-магазина"):
        shop_driver.get("https://www.saucedemo.com/")
        page = ShopPage(shop_driver)

    with allure.step("Авторизоваться"):
        page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        page.add_items()

    with allure.step("Проверить что в корзине три товара"):
        assert page.get_cart_count() == "3"

    with allure.step("Перейти в корзину"):
        page.go_to_cart()

    with allure.step("Нажать на кнопку Checkout"):
        page.proceed_to_checkout()

    with allure.step("Заполнить поля информацией о покупателе "):
        page.fill_checkout_info("Юлия", "Хрусталева", "142506")

    with allure.step("Нажать кнопку Continue"):
        page.click_continue()

    with (allure.step("Проверить итоговую сумму заказа")):
        total_text = page.get_total_text()
        assert "Total: $58.29" in total_text, (
            f"Ожидалась сумма $58.29, "
            f"но на странице отображается: {total_text}"
        )

    with allure.step("Нажать кнопку Finish"):
        page.click_finish()

    with allure.step("Проверить, что отображается страница успешного заказа"):
        assert page.is_complete_page_displayed()

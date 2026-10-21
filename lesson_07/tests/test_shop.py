from lesson_07.pages.shop_page import ShopPage


def test_shopping(shop_driver):
    shop_driver.get("https://www.saucedemo.com/")
    page = ShopPage(shop_driver)

    page.login("standard_user", "secret_sauce")
    page.add_items()
    assert page.get_cart_count() == "3"
    page.go_to_cart()
    page.proceed_to_checkout()

    page.fill_checkout_info("Юлия", "Хрусталева", "142506")
    page.click_continue()

    total_text = page.get_total_text()
    assert "Total: $58.29" in total_text, f"Ожидалась сумма $58.29, но на странице отображается: {total_text}"

    page.click_finish()
    assert page.is_complete_page_displayed()

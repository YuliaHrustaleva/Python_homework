from lesson_07.pages.calc_page import CalcPage


def test_calculate(calc_driver):
    calc_driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    page = CalcPage(calc_driver)

    page.set_delay(45)
    page.press_buttons(["7", "+", "8", "="])
    page.wait_result("15", timeout=46)

    result = page.get_result()
    assert result == "15"










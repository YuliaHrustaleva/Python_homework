from pages.calc_page import CalcPage
import allure


@allure.feature("Калькулятор")
@allure.title("Проверка работы калькулятора")
@allure.description("Тест устанавливает задержку, вводит выражение, "
                    "ожидает и проверяет итоговый результат")
@allure.severity(allure.severity_level.NORMAL)
def test_calculate(calc_driver):

    with allure.step("Перейти на страницу калькулятора"):
        calc_driver.get(
            "https://bonigarcia.dev"
            "slow-calculator.html"
        )
        page = CalcPage(calc_driver)

    with allure.step("Установить задержку 45 секунд"):
        page.set_delay(45)

    with allure.step("Ввести выражение: 7+8="):
        page.press_buttons(["7", "+", "8", "="])

    with allure.step("Ожидать результат"):
        page.wait_result("15", timeout=46)

    with allure.step("проверить итоговый результат"):
        result = page.get_result()
        assert result == "15"

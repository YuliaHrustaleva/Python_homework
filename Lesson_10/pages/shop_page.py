from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ShopPage(BasePage):
    # Локаторы авторизации
    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    # Локаторы товаров
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")

    # Локаторы корзины и чекаута
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BTN = (By.ID, "checkout")

    # Локаторы формы чекаута
    FNAME = (By.ID, "first-name")
    LNAME = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")

    # Локаторы результатов
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def login(self, username: str, password: str) -> None:
        """Авторизоваться в системе под указанными данными"""
        self.wait_for_presence(self.USER_NAME).send_keys(username)
        self.wait_for_presence(self.PASSWORD).send_keys(password)
        self.wait_for_element_clickable(self.LOGIN_BTN).click()

    def add_items(self) -> None:
        """Добавить три определенных товара"""
        self.wait_for_element_clickable(self.BACKPACK).click()
        self.wait_for_element_clickable(self.BOLT_TSHIRT).click()
        self.wait_for_element_clickable(self.ONESIE).click()

    def get_cart_count(self) -> str:
        """Получить значение количества товара на иконке корзины"""
        return self.wait_for_presence(self.CART_BADGE).text

    def go_to_cart(self) -> None:
        """Перейти в корзину, кликнув на иконку корзины"""
        self.wait_for_element_clickable(self.CART_LINK).click()

    def proceed_to_checkout(self) -> None:
        """Нажать кнопку оформления заказа"""
        self.wait_for_element_clickable(self.CHECKOUT_BTN).click()

    def fill_checkout_info(self, fname: str, lname: str, postal: str) -> None:
        """Заполнить поля формы данными о покупателе"""
        self.wait_for_presence(self.FNAME).send_keys(fname)
        self.wait_for_presence(self.LNAME).send_keys(lname)
        self.wait_for_presence(self.POSTAL).send_keys(postal)

    def click_continue(self) -> None:
        """Нажать на кнопку Continue"""
        self.wait_for_element_clickable(self.CONTINUE_BTN).click()

    def get_total_text(self) -> str:
        """Проверить итоговую (TOTAL) сумму заказа"""
        return self.wait_for_presence(self.TOTAL_LABEL).text

    def click_finish(self) -> None:
        """Нажать на кнопку FINISH для подтверждения заказа"""
        self.wait_for_element_clickable(self.FINISH_BTN).click()

    def is_complete_page_displayed(self) -> bool:
        """Проверить, что отображается заголовок успешно созданного заказа"""
        return self.wait_for_presence(self.COMPLETE_HEADER).is_displayed()

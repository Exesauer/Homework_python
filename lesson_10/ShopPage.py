from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep
import allure

class ShopPage:
    """Класс для взаимодействия с магазином на веб-странице."""

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы магазина.

        Аргументы:
            driver (WebDriver): веб-драйвер для взаимодействия с элементами страницы.
        """
        self.driver = driver

    def authorization(self, login: str, password: str) -> None:
        """
        Авторизация пользователя.

        Аргументы:
            login (str): логин пользователя.
            password (str): пароль пользователя.
        """
        allure.attach(login, name="Логин", attachment_type=allure.attachment_type.TEXT)
        allure.attach(password, name="Пароль", attachment_type=allure.attachment_type.TEXT)

        self.login = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'user-name'))
        ).send_keys(login)
        
        self.password = self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()
        sleep(5) # Задержка для ручного закрытия сообщения браузера об утечке пароля
    
    def add_to_cart(self, *products: str) -> None:
        """
        Добавление указанных продуктов в корзину.

        Аргументы:
            *products (str): идентификаторы продуктов.
        """
        allure.attach(", ".join(products), name="Продукты", attachment_type=allure.attachment_type.TEXT)
        for product in products:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, product))
            ).click()

    def cart_and_checkout(self) -> None:
        """
        Переход в корзину и на страницу оформления заказа.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'checkout'))
        ).click()

    def input_form_data(self, name: str, last_name: str, postal_code: str) -> None:
        """
        Ввод данных пользователя для оформления заказа.

        Аргументы:
            name (str): имя пользователя.
            last_name (str): фамилия пользователя.
            postal_code (str): почтовый индекс пользователя.
        """
        allure.attach(name, name="Имя", attachment_type=allure.attachment_type.TEXT)
        allure.attach(last_name, name="Фамилия", attachment_type=allure.attachment_type.TEXT)
        allure.attach(postal_code, name="Почтовый индекс", attachment_type=allure.attachment_type.TEXT)

        self.name = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'first-name'))
        ).send_keys(name)
        self.last_name = self.driver.find_element(By.ID, 'last-name').send_keys(last_name)
        self.postal_code = self.driver.find_element(By.ID, 'postal-code').send_keys(postal_code)

    def press_continue(self) -> None:
        """
        Нажатие кнопки 'Продолжить' на странице оформления.
        """
        self.driver.find_element(By.ID, 'continue').click()

    def total_amount(self) -> str:
        """
        Получение итоговой суммы заказа.

        Возвращает:
            str: итоговая сумма, указанная на странице.
        """
        total = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label')))
        total_amount_text = total.text
        allure.attach(total_amount_text, name="Итоговая сумма заказа", attachment_type=allure.attachment_type.TEXT)
        return total_amount_text
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import allure

class CalcPage:
    """Класс для взаимодействия с калькулятором на веб-странице."""

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы калькулятора.

        Аргументы:
            driver (WebDriver): веб-драйвер для взаимодействия с элементами страницы.
        """
        self.driver = driver

    def input_delay(self, delay_time: int) -> None:
        """
        Ввод значения задержки на странице.

        Аргументы:
            delay_time (int): значение задержки, введенное как строка.
        """
        self.delay = self.driver.find_element(By.ID, "delay")
        self.delay.clear()
        self.delay.send_keys(delay_time)
        allure.attach(str(delay_time), "Введенное значение задержки", allure.attachment_type.TEXT)

    def pressing_buttons(self, button: str) -> None:
        """
        Нажатие на кнопку на калькуляторе.

        Аргументы:
            button (str): текст на кнопке, которая будет нажата.
        """
        button_element = self.driver.find_element(By.XPATH, f"//span[contains(@class, 'btn') and text()='{button}']")
        button_element.click()
        allure.attach(button, "Нажатая кнопка", allure.attachment_type.TEXT)

    def taimer_and_wait(self) -> float:
        """
        Ожидание завершения работы калькулятора и измерение времени.

        Возвращает:
            float: время ожидания в секундах.
        """
        start_time = time.time()        # Запоминаем время начала ожидания
        allure.attach(str(start_time), "Время начала ожидания", allure.attachment_type.TEXT)
        self.wait_for_spinner()         # Ожидаем пока не исчезнет спиннер
        end_time = time.time()          # Запоминаем время, когда спиннер исчез
        allure.attach(str(end_time), "Время окончания ожидания исчезновения спиннера", allure.attachment_type.TEXT)
        elapsed = end_time - start_time # Запоминаем время завершения ожидания
        allure.attach(str(elapsed), "Время ожидания", allure.attachment_type.TEXT)
        return elapsed

    def wait_for_spinner(self, timeout: int = 100) -> None:
        """
        Ожидание исчезновения спиннера загрузки.

        Аргументы:
            timeout (int): максимальное время ожидания в секундах.
        """
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(By.ID, "spinner").value_of_css_property('display') == 'none'
        )
        allure.attach(f"Спиннер ожидания исчез", "Фаза ожидания", allure.attachment_type.TEXT)

    def check_screen(self) -> WebElement:
        """
        Проверка экрана калькулятора на наличие результата.

        Возвращает:
            WebElement: элемент веб-страницы с результатом вычисления.
        """
        self.result = self.driver.find_element(By.CLASS_NAME, "screen")
        allure.attach(self.result.text, "Результат проверки экрана калькулятора", allure.attachment_type.TEXT)
        return self.result
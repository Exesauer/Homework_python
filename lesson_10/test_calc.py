import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage
import allure

@pytest.fixture
def driver():
    """
    Фикстура для инициализации веб-драйвера Chrome.

    - Устанавливает и запускает веб-драйвер Chrome.
    - Открывает сайт https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html.
    - Максимизирует окно браузера.
    - Закрывает браузер после выполнения тестов.
    """
    # Устанавливаем драйвер Chrome с использованием менеджера драйверов
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # Максимизируем окно браузера для лучшей видимости элементов управления
    driver.maximize_window() 
    
    # Открываем заданный URL в браузере
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Возвращаем драйвер для использования в тестах и завершаем работу после теста
    yield driver
    
    # Закрываем браузер после завершения тестов
    driver.quit()

@allure.feature("Калькулятор")
@allure.story("Тестирование операций сложения")
class TestCalculator:
    """Класс тестов для калькулятора."""

    DELAY_VALUE = 5  # Определяем DELAY_VALUE как константу класса
    sum_expected = 15 # Определяем sum_expected как константу класса

    @allure.title("Проверка сложения: 7 + 8")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_calc(self, driver: webdriver.Chrome) -> None:
        """
        Тест на проверку корректности операции сложения на калькуляторе.

        Аргументы:
            driver (webdriver.Chrome): веб-драйвер для взаимодействия с калькулятором.
        """
        
        with allure.step("Создание страницы калькулятора"):
            page = CalcPage(driver)
        
        with allure.step("Ввод задержки"):
            page.input_delay(self.DELAY_VALUE)

        with allure.step("Нажатие кнопок для сложения 7 и 8"):
            page.pressing_buttons('7')
            page.pressing_buttons('+')
            page.pressing_buttons('8')
            page.pressing_buttons('=')

        with allure.step("Ожидание результата"):
            taimer = page.taimer_and_wait()
        
        with allure.step("Проверка результата на экране"):
            result = page.check_screen()

        with allure.step("Проверка корректности результата и времени ожидания"):
            assert result.text.strip() == str(self.sum_expected), f"Результат ({result.text}) не равен {self.sum_expected}"
            assert round(taimer) == self.DELAY_VALUE, f"Время ожидания ({round(taimer)}) не равно {self.DELAY_VALUE}"
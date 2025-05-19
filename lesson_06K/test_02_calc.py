import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Фикстура для создания и закрытия экземпляра драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

# Ожидание, пока спиннер исчезнет с экрана (display: none)
def wait_for_spinner(driver, timeout=100):
    WebDriverWait(driver, timeout).until(
        lambda d: d.find_element(By.ID, "spinner").value_of_css_property('display') == 'none'
    )

# Тест для проверки сложения в "медленном калькуляторе" с задержкой
def test_slow_calculator_addition(driver):

    DELAY_VALUE = 5  # Ожидаемая задержка (секунды)
    num_1 = 7
    num_2 = 8
    sum_nums = num_1 + num_2

    # Открываем страницу калькулятора
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    # Выставляем задержку
    delay = driver.find_element(By.ID, "delay")
    delay.clear()
    delay.send_keys(DELAY_VALUE)

    # Вводим первое число
    driver.find_element(By.XPATH, f"//span[contains(@class, 'btn') and text()='{num_1}']").click()
    # Нажимаем кнопку сложения
    driver.find_element(By.XPATH, "//span[contains(@class, 'btn') and text()='+']").click()
    # Вводим второе число
    driver.find_element(By.XPATH, f"//span[contains(@class, 'btn') and text()='{num_2}']").click()
    # Нажимаем "=" для получения результата
    driver.find_element(By.XPATH, "//span[contains(@class, 'btn') and text()='=']").click()

    # Засекаем время ожидания
    start_time = time.time()
    wait_for_spinner(driver)
    end_time = time.time()
    elapsed = end_time - start_time

    # Проверяем, что результат соответствует ожидаемому значению
    result = driver.find_element(By.CLASS_NAME, "screen")
    assert result.text.strip() == str(sum_nums), f"Результат ({result.text}) не равен {sum_nums}"
    # Проверяем, что время ожидания примерно равно указанной задержке
    assert round(elapsed) == DELAY_VALUE, f"Время ожидания ({round(elapsed)}) не равно {DELAY_VALUE}"
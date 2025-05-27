import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from CalcPage import CalcPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

def test_calc(driver: WebDriver):
    sum = 15
    DELAY_VALUE = 45

    page = CalcPage(driver)
    page.input_delay(DELAY_VALUE)

    page.pressing_buttons('7')
    page.pressing_buttons('+')
    page.pressing_buttons('8')
    page.pressing_buttons('=')

    taimer = page.taimer_and_wait()
    result = page.check_screen()

    assert result.text.strip() == str(sum), f"Результат ({result.text}) не равен {sum}"
    assert round(taimer) == DELAY_VALUE, f"Время ожидания ({round(taimer)}) не равно {DELAY_VALUE}"
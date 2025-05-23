import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Настройка Chrome и отключение лишних уведомлений
    options = Options()
    options.add_experimental_option("excludeSwitches", [
        "enable-automation", 
        "enable-logging",
        "enable-password-manager-reauthentication"
    ])
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()

def test_saucedemo_cart_total(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    # Вход
    wait.until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys('standard_user')
    wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    # Добавление товаров в корзину
    wait.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-backpack'))).click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    # Корзина и оформление заказа
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'checkout'))).click()

    wait.until(EC.visibility_of_element_located((By.ID, 'first-name'))).send_keys('Vladimir')
    driver.find_element(By.ID, 'last-name').send_keys('Shchemelev')
    driver.find_element(By.ID, 'postal-code').send_keys('190000')
    driver.find_element(By.ID, 'continue').click()

    # Проверка суммы
    total = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label')))
    assert total.text == 'Total: $58.29', f"Итоговая сумма {total.text} не равна $58.29"
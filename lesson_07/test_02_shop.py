import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from ShopPage import ShopPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_shop(driver):
    page = ShopPage(driver)
    page.authorization('standard_user', 'secret_sauce')
    page.add_to_cart(
    'add-to-cart-sauce-labs-backpack',
    'add-to-cart-sauce-labs-bolt-t-shirt',
    'add-to-cart-sauce-labs-onesie')
    page.cart_and_checkout()
    page.input_form_data('Vladimir', 'Shchemelev', '190000')
    page.press_continue()
    total_amount = page.total_amount()
    assert total_amount == 'Total: $58.29', f"Итоговая сумма {total_amount} не равна $58.29"
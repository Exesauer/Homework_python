import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from ShopPage import ShopPage
import allure

@pytest.fixture
def driver():
    """
    Фикстура для инициализации веб-драйвера Chrome.

    - Устанавливает и запускает веб-драйвер Chrome.
    - Открывает сайт https://www.saucedemo.com/.
    - Максимизирует окно браузера.
    - Закрывает браузер после выполнения тестов.
    """
    # Устанавливаем драйвер Chrome с использованием менеджера драйверов
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # Максимизируем окно браузера для лучшей видимости элементов
    driver.maximize_window()
    
    # Открываем заданный URL в браузере
    driver.get("https://www.saucedemo.com/")
    
    # Возвращаем драйвер для использования в тестах и завершаем работу после теста
    yield driver
    driver.quit()

@allure.feature("Магазин")
@allure.story("Тестирование покупки товаров")
class TestShop:

    @allure.title("Проверка процесса покупки товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_shop(self, driver: webdriver.Chrome):
        """
        Тест на проверку процесса покупки товаров в магазине.

        Аргументы:
            driver (webdriver.Chrome): веб-драйвер для взаимодействия с магазином.
        """
        
        with allure.step("Создание страницы магазина"):
            page = ShopPage(driver)

        with allure.step("Авторизация пользователя"):
            page.authorization('standard_user', 'secret_sauce')

        with allure.step("Добавление товаров в корзину"):
            page.add_to_cart(
                'add-to-cart-sauce-labs-backpack',
                'add-to-cart-sauce-labs-bolt-t-shirt',
                'add-to-cart-sauce-labs-onesie'
            )

        with allure.step("Переход в корзину и оформление заказа"):
            page.cart_and_checkout()

        with allure.step("Ввод данных для оформления заказа"):
            page.input_form_data('Vladimir', 'Shchemelev', '190000')
        
        with allure.step("Подтверждение продолжения на странице заказа"):
            page.press_continue()

        with allure.step("Проверка итоговой суммы заказа"):
            total_amount = page.total_amount()
        
        with allure.step("Проверка совпадения итоговой суммы"):
            assert total_amount == 'Total: $58.29', f"Итоговая сумма {total_amount} не равна $58.29"
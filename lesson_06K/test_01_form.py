import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Фикстура для инициализации и закрытия браузера
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

# Тест на проверку подсветки полей формы
def test_form_fields_highlight(driver):
    # Открываем нужную страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Тестовые данные для заполнения формы; поле zip-code специально оставляем пустым
    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "job-position": "QA",
        "company": "SkyPro"
    }

    # Заполняем поля формы тестовыми данными
    for name, value in form_data.items():
        field = driver.find_element(By.NAME, name)
        field.clear()  # Очищаем поле перед вводом
        field.send_keys(value)  # Вводим значение

    # Отправляем форму
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверяем подсветку границы у каждого поля
    for id, value in form_data.items():
        field = driver.find_element(By.ID, id)  # Находим поле по id
        border_color = field.value_of_css_property("border-color")  # Получаем цвет границы

        if value:
            # Для заполненных полей ожидаем зеленую подсветку
            assert border_color == "rgb(186, 219, 204)", f"Ожидался зеленый, но у поля {id} цвет {border_color}"
        else:
            # Для пустых полей ожидаем красную
            assert border_color == "rgb(245, 194, 199)", f"Ожидался красный, но у поля {id} цвет {border_color}"
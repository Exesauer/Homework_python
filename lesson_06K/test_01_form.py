from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

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

for name, value in form_data.items():
    field = driver.find_element(By.NAME, name)
    field.clear()
    field.send_keys(value)

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

for id, value in form_data.items():
    field = driver.find_element(By.ID, id)
    border_color = field.value_of_css_property("border-color")
    
    if value:
        assert border_color == "rgb(186, 219, 204)"
        print(f"Поле {id} подсвечено зеленым 🟢")
    else:
        assert border_color == "rgb(245, 194, 199)"
        print(f"Поле {id} подсвечено красным 🔴")

driver.quit()



from time import sleep# Использую тут слип, потому что после авторизации высвечивается всплывающее окно об утечке пароля, которое блокирует выполнение кода. Не разобрался как автоматически принимать его, буду рад подсказке.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")

user_name = driver.find_element(By.ID, 'user-name')
user_name.clear()
user_name.send_keys('standard_user')

password = driver.find_element(By.ID, 'password')
password.clear()
password.send_keys('secret_sauce')

driver.find_element(By.ID, 'login-button').click()
sleep(5)
driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

driver.find_element(By.ID, 'checkout').click()

first_name = driver.find_element(By.ID, 'first-name')
first_name.clear()
first_name.send_keys('Vladimir')

last_name = driver.find_element(By.ID, 'last-name')
last_name.clear()
last_name.send_keys('Shchemelev')

postal_code = driver.find_element(By.ID, 'postal-code')
postal_code.clear()
postal_code.send_keys('190000')

driver.find_element(By.ID, 'continue').click()

total = driver.find_element(By.CLASS_NAME, 'summary_total_label')
print(total.text)

assert total.text == 'Total: $58.29', f"Итоговая сумма {total} не равна $58.29"

driver.quit()
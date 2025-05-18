import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

DELAY_VALUE = 45
num_1 = 7
num_2 = 8
sum_nums = num_1 + num_2

delay = driver.find_element(By.ID, "delay")
delay.clear()
delay.send_keys(DELAY_VALUE)

driver.find_element(By.XPATH, f"//span[contains(@class, 'btn') and text()='{num_1}']").click()
driver.find_element(By.XPATH, "//span[contains(@class, 'btn') and text()='+']").click()
driver.find_element(By.XPATH, f"//span[contains(@class, 'btn') and text()='{num_2}']").click()
driver.find_element(By.XPATH, "//span[contains(@class, 'btn') and text()='=']").click()

def wait_for_spinner(driver, timeout=100):
    WebDriverWait(driver, timeout).until(
        lambda d: d.find_element(By.ID, "spinner").value_of_css_property('display') == 'none'
    )

start_time = time.time()
wait_for_spinner(driver)
end_time = time.time()
elapsed = end_time - start_time

result = driver.find_element(By.CLASS_NAME, "screen")
assert result.text.strip() == str(sum_nums), f"Результат ({result}) не равен {sum_nums}"
assert round(elapsed) == DELAY_VALUE, f"Время ожидания ({round(elapsed)}) не равно {DELAY_VALUE}"
print(f"Результат: {result.text}")
print(f"Время ожидания: {round(elapsed)} секунд")

driver.quit()
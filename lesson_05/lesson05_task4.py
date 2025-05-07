from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/login")

input_box = driver.find_element(By.CSS_SELECTOR, "input#username")
input_box.send_keys("tomsmith")
sleep(1)

input_box = driver.find_element(By.CSS_SELECTOR, "input#password")
input_box.send_keys("SuperSecretPassword!")
sleep(1)

button = driver.find_element(By.CSS_SELECTOR, '.radius')
button.click()
sleep(1)

green_box = driver.find_element(By.CSS_SELECTOR, "div#flash")

message = green_box.text.split("×")[0].strip()
print(message)

driver.quit()

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/inputs")

input_box = driver.find_element(By.TAG_NAME, "input")

input_box.send_keys("Sky")
sleep(1)
input_box.clear()

input_box.send_keys("Pro")

sleep(1)
driver.quit()
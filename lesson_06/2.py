from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

x = driver.find_element(By.ID, "newButtonName")
x.send_keys("SkyPro")

click = driver.find_element(By.ID, "updatingButton").click()

sleep(1)

y = driver.find_element(By.ID, "updatingButton")
print(y.text)

sleep(1)

driver.quit()
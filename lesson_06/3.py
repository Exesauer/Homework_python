from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

compass = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'compass')))
calendar = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'calendar')))
award = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'award')))
landscape = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'landscape')))

attribute_award = award.get_attribute('src')

print(attribute_award)

driver.quit()


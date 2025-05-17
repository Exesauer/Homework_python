from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")

x = driver.find_element(By.ID, "ajaxButton").click()

x = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'bg-success')))

print(x.text)

driver.quit()
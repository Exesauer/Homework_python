import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class CalcPage:
    def __init__(self, driver):
        self.driver = driver

    def input_delay(self, delay_time):
        self.delay = self.driver.find_element(By.ID, "delay")
        self.delay.clear()
        self.delay.send_keys(delay_time)

    def pressing_buttons(self, button):
        self.button = self.driver.find_element(By.XPATH, f"//span[contains(@class, 'btn') and text()='{button}']").click()

    def taimer_and_wait(self):
        start_time = time.time()
        self.wait_for_spinner()
        end_time = time.time()
        elapsed = end_time - start_time
        return elapsed

    def wait_for_spinner(self, timeout=100):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(By.ID, "spinner").value_of_css_property('display') == 'none'
            )

    def check_screen(self):
        self.result = self.driver.find_element(By.CLASS_NAME, "screen")
        return self.result
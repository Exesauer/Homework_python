from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login, password):
        self.login = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys(f'{login}')
        self.password = self.driver.find_element(By.ID, 'password').send_keys(f'{password}')
        self.driver.find_element(By.ID, 'login-button').click()
        sleep(5)

    def add_to_cart(self, *products):
        for product in products:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, product))
            ).click()

    def cart_and_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'checkout'))).click()

    def input_form_data(self, name, last_name, postal_code):
        self.name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'first-name'))).send_keys(f'{name}')
        self.last_name = self.driver.find_element(By.ID, 'last-name').send_keys(f'{last_name}')
        self.postal_code = self.driver.find_element(By.ID, 'postal-code').send_keys(f'{postal_code}')

    def press_continue(self):
        self.driver.find_element(By.ID, 'continue').click()

    def total_amount(self):
        total = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'summary_total_label')))
        return total.text
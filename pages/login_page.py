from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

class OrangeHRM:
    def __init__(self, driver):
        self.driver = driver
        self.faker = Faker()

    def open_chrome(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

    def put_username_and_password(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Username']"))
        )
        username_field.click()
        username_field.send_keys(username)

        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))
        )
        password_field.click()
        password_field.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()=' Login ']"))
        )
        login_button.click()

    def invalid_login_data(self, username, password):
        username = self.faker.user_name()
        password = self.faker.password()

        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Username']"))
        )
        username_field.clear()
        username_field.send_keys(username)

        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Password']"))
        )
        password_field.clear()
        password_field.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()=' Login ']"))
        )
        login_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='alert'] p"))
        )

        assert error_message.is_displayed()
        assert "Invalid credentials" in error_message.text


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OpenPIM:
    def __init__(self, driver):
        self.driver = driver

    def open_PIM(self):
        pim_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']/.."))
        )
        pim_button.click()



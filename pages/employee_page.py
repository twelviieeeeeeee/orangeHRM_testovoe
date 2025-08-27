import time
import re
from faker import Faker
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class EmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.faker = Faker()
        self.last_employee_data = {}

    def add_employee(self):
        add_employee = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Add')]]"))
        )
        add_employee.click()

        first_name = self.faker.first_name()
        middle_name = self.faker.first_name()
        last_name = self.faker.last_name()
        employee_id = self.faker.random_int(min=1000, max=9999)

        input_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='First Name']"))
        )
        input_firstname.send_keys(first_name)

        input_middlename = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Middle Name']"))
        )
        input_middlename.send_keys(middle_name)

        # lastname
        input_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Last Name']"))
        )
        input_lastname.send_keys(last_name)

        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Save')]]"))
        )
        save_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h6[text()='Personal Details']"))
        )

        self.last_employee_data.update({
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "full_name": f"{first_name} {last_name}"
        })

    def open_employee_list_and_find(self):
        employee_list_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Employee List']"))
        )
        employee_list_tab.click()

        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))
        )
        search_input.click()
        search_input.clear()
        search_input.send_keys(self.last_employee_data["last_name"])

        time.sleep(1)

        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Search')]]"))
        )
        search_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-table-body"))
        )

        try:
            row = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, f"""
                      //div[@role='row'][
                          .//div[contains(., '{self.last_employee_data['first_name']}')] and
                          .//div[contains(., '{self.last_employee_data['last_name']}')]
                      ]
                  """))
            )
            assert row.is_displayed(), "Employee doesnt exist"
            print(f"Employee {self.last_employee_data['full_name']} found in list ")
        except Exception as e:
            pytest.fail(f"Employee not found: {e}")

    def change_email(self):
        add_employee = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Add')]]"))
        )
        add_employee.click()

        first_name = self.faker.first_name()
        middle_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = self.faker.email()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='First Name']"))
        ).send_keys(first_name)

        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Middle Name']").send_keys(middle_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']").send_keys(last_name)

        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Save')]]"))
        )

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader"))
        )
        save_button.click()

        contact_tab = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Contact Details"))
        )
        contact_tab.click()

        email_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[text()='Work Email']/following::input[1]"))
        )
        email_input.clear()
        email_input.send_keys(email)

        save_button_contact = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Save')]]"))
        )
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader"))
        )
        save_button_contact.click()

        success_message = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-toast--success')]"))
        )
        assert success_message.is_displayed(), "Successfully Updated"
        print("Successfully Updated")

    def successfull_messages_masks_input_fields(self):
        add_employee = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Add')]]"))
        )
        add_employee.click()

        first_name = self.faker.first_name()
        middle_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = self.faker.email()

        input_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='First Name']"))
        )
        input_firstname.send_keys(first_name)

        input_middlename = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Middle Name']"))
        )
        input_middlename.send_keys(middle_name)

        # lastname
        input_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Last Name']"))
        )
        input_lastname.send_keys(last_name)

        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Save')]]"))
        )
        save_button.click()

        job_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Contact Details"))
        )
        job_button.click()

        email_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[text()='Work Email']/following::input[1]"))
        )
        email_input.click()
        email_input.send_keys(email)
        assert email_input.is_displayed(), "Expected format: admin@example.com"

        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Save')]]"))
        )
        save_button.click()

        phone_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Home']/following::input[1]"))
        )
        phone_input.send_keys("abc123")
        value = phone_input.get_attribute("value")
        assert "123" in value, "Allows numbers and only + - / ( )"

    def logout(self):
        profile_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.oxd-userdropdown-tab"))
        )
        profile_dropdown.click()

        logout_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Logout"))
        )
        logout_button.click()

    def create_employee_without_fields(self):
        add_employee = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Add')]]"))
        )
        add_employee.click()

        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Save')]]"))
        )
        save_button.click()

        required_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "span.oxd-input-field-error-message")
            )
        )
        assert required_message.is_displayed()
        assert required_message.text == "Required"

    def empty_field_in_search(self):
        employee_list_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Employee List']"))
        )
        employee_list_tab.click()

        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Search')]]"))
        )
        search_button.click()

    def verify_that_changes_is_saved_and_changes_not_saved(self):
        user_name = self.faker.user_name()
        admin_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[.//span[text()='Admin']]")
            )
        )
        admin_menu.click()

        edit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "(//div[contains(@class,'oxd-table-cell-actions')]//button[i[contains(@class,'bi-pencil-fill')]])[1]")
            )
        )
        self.driver.execute_script("arguments[0].click();", edit_button)

        new_username = self.faker.user_name()

        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[text()='Username']/following::input[1]")
            )
        )
        username_input.click()
        username_input.send_keys(new_username)

        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Save')]]"))
        )
        save_button.click()

        edit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "(//div[contains(@class,'oxd-table-cell-actions')]//button[i[contains(@class,'bi-pencil-fill')]])[1]")
            )
        )
        self.driver.execute_script("arguments[0].click();", edit_button)

        cancel_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., 'Cancel')]]"))
        )
        cancel_button.click()







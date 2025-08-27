import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest_html
from selenium import webdriver
from pages.pim_page import OpenPIM
from pages.login_page import OrangeHRM
from pages.employee_page import EmployeePage



@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def login_data():
    return {
        "username": "Admin",
        "password": "admin123"
    }


@pytest.fixture
def authenticated_driver(driver, login_data):
    hrm = OrangeHRM(driver)
    hrm.open_chrome()
    hrm.put_username_and_password(login_data["username"], login_data["password"])
    return driver

@pytest.fixture
def pim_authenticated_driver(authenticated_driver):
    pim = OpenPIM(authenticated_driver)
    pim.open_PIM()
    return authenticated_driver


@pytest.fixture
def employee_created(pim_authenticated_driver):
    emp = EmployeePage(pim_authenticated_driver)
    emp.add_employee()
    return pim_authenticated_driver, emp


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs['driver']
        screenshot = f"screenshots/{item.name}.png"
        driver.save_screenshot(screenshot)
        if hasattr(rep, "extra"):
            rep.extra.append(pytest_html.extras.png(screenshot))



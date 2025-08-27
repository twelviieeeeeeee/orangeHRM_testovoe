import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import OrangeHRM
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Логин валидными данными
def test_login(driver, login_data):
    hrm = OrangeHRM(driver)
    hrm.open_chrome()
    hrm.put_username_and_password(login_data["username"], login_data["password"])
#Это чтоб проверить,что вошло
def test_verify_dashboard(driver, login_data):
    hrm = OrangeHRM(driver)
    hrm.open_chrome()
    hrm.put_username_and_password(login_data["username"], login_data["password"])

    dashboard = DashboardPage(driver)
    dashboard.verify_dashboard()
# Неверный логин/пароль — проверка текста и стиля ошибки
def test_invalid_logi_data(driver, login_data):
    hrm = OrangeHRM(driver)
    hrm.open_chrome()
    hrm.invalid_login_data(login_data["username"], login_data["password"])

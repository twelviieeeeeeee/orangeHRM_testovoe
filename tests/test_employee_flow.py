import pytest
from pages.pim_page import OpenPIM
from pages.login_page import OrangeHRM
from pages.employee_page import EmployeePage
from tests.conftest import login_data

# Переход в модуль PIM и создание сотрудника
def test_open_pim_and_add_employee(pim_authenticated_driver):
    emp = EmployeePage(pim_authenticated_driver)
    emp.add_employee()


# Проверка: сотрудник появился в списке (по ФИО/ID).
def test_find_employee_with_name(employee_created):
    driver, emp = employee_created
    emp.open_employee_list_and_find()


# Редактирование профиля сотрудника (например, должность/статус)
def test_change_employee_status(pim_authenticated_driver):
    emp = EmployeePage(pim_authenticated_driver)
    emp.add_employee()
    emp.change_email()


# Валидации UI: сообщения об успехе, маски ввода, обязательные поля
def test_success_message_mask_and_input_field(pim_authenticated_driver):
    emp = EmployeePage(pim_authenticated_driver)
    emp.add_employee()
    emp.successfull_messages_masks_input_fields()


# Логаут.
def test_logout_button(authenticated_driver):
    emp = EmployeePage(authenticated_driver)
    emp.logout()

# Негативные тесты
# Негативный на логин находится в файле тест-логин

# Создание сотрудника без обязательных полей — валидации форм
def test_employee_without_fields(pim_authenticated_driver):
    emp = EmployeePage(pim_authenticated_driver)
    emp.create_employee_without_fields()
# Поиск несуществующего сотрудника — пустые результаты и отсутствие ошибок в консоли
def test_invalid_id_in_search(pim_authenticated_driver):
    emp = EmployeePage(pim_authenticated_driver)
    emp.empty_field_in_search()
# Проверка сохранения/отмены изменений на форме редактирования
def test_change_and_cancel(authenticated_driver):
    emp = EmployeePage(authenticated_driver)
    emp.verify_that_changes_is_saved_and_changes_not_saved()

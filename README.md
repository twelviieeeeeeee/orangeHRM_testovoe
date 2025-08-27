# ​ OrangeHRM Test Automation

Этот репозиторий содержит тесты UI для OrangeHRM, реализованные с помощью Selenium и PyTest,всего тестов 11, полный стек:

Selenium, Pytest, Faker, Pytest-html

Мое окружения для тестов:

platform win32 -- Python 3.13.3, pytest-8.4.1, pluggy-1.6.0

rootdir: C:\Users\Twelve\PycharmProjects\ui_testovoe

plugins: Faker-37.6.0, html-4.1.1, metadata-3.1.1

Как устанавливать зависимости:

- Установленные зависимости:  

  ```bash

  pip install -r requirements.txt

Все настройки (baseUrl, креды и т.п.) хранятся в файле **`settings.py`** в папке config

```python
BASE_URL = "https://opensource-demo.orangehrmlive.com"

VALID_USERNAME = "Admin"

VALID_PASSWORD = "admin123"

  Запуск тестов:

pip install pytest-html 

pytest --html=report.html --self-contained-html




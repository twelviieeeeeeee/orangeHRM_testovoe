# OrangeHRM UI Test Automation

Набор UI-автотестов для демо-стенда [OrangeHRM](https://opensource-demo.orangehrmlive.com), реализованный на **Selenium + PyTest**.

## 📦 Стек
- Selenium
- PyTest
- Faker (генерация тестовых данных)
- Pytest-html (репорты)

## 🖥️ Окружение
Тесты разрабатывались и запускались в следующем окружении:
```
- Windows 10 / Python 3.13.3

- pytest 8.4.1

- pluggy 1.6.0

- faker 37.6.0

- pytest-html 4.1.1

- pytest-metadata 3.1.1
```
## 📂 Структура проекта
```
.
├── config/

│ └── settings.py # Конфигурация: baseUrl, креды, браузер

├── pages/ # Page Object классы (LoginPage, PIMPage, EmployeePage и др.)

├── tests/ # Тесты

│ ├── conftest.py # фикстуры, хуки, скриншоты при падении
│ └── ... # e2e и негативные тесты

├── utils/ # вспомогательные функции (генерация данных и др.)

├── requirements.txt

└── README.md
```


## ⚙️ Конфигурация
Все настройки хранятся в `config/settings.py`:
```python
BASE_URL = "https://opensource-demo.orangehrmlive.com/"

VALID_USERNAME = "Admin"

VALID_PASSWORD = "admin123"

BROWSER = "chrome" 

HEADLESS = False
```
Установка и запуск:

```
Клонирование и запуск:

git clone https://github.com/twelviieeeeeeee/orangeHRM_testovoe.git
cd orangeHRM_testovoe
```
```
Установить зависимости:

pip install -r requirements.txt
```
```
Запустить все тесты с HTML-отчетом:

pytest --html=report.html --self-contained-html
```
Скриншоты падений сохраняются в tests/screenshots/ автоматически.

Покрытие тестов

Реализовано 11 тестов:
```
Позитивные:

Авторизация валидными данными

Переход в PIM и создание сотрудника

Поиск сотрудника по имени

Редактирование профиля сотрудника

Проверка сообщений об успехе, масок и обязательных полей

Логаут
```
```
Негативные:

Неверный логин 

Создание сотрудника без обязательных полей 

Поиск несуществующего сотрудника

Проверка сохранения/отмены изменений 
```
Так же несколько тестов на логин по тз
```
Артефакты

HTML-репорт (report.html)

Скриншоты при падении: tests/screenshots/
```
Автор: Диана Мухортова


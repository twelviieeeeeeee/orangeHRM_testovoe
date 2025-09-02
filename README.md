# OrangeHRM UI Test Automation

A set of UI automation tests for the [OrangeHRM](https://opensource-demo.orangehrmlive.com), demo site, implemented with Selenium + PyTest.

## 📦 Stack
- Selenium
- PyTest
- Faker (test data generation)
- Pytest-html (reports)

## 🖥️ Environment
Tests were developed and executed in the following environment:
```
- Windows 10 / Python 3.13.3

- pytest 8.4.1

- pluggy 1.6.0

- faker 37.6.0

- pytest-html 4.1.1

- pytest-metadata 3.1.1
```
## 📂Project Structure
```
.
├── config/

│ └── settings.py # Configuration: baseUrl, credentials, browser

├── pages/ # Page Object classes (LoginPage, PIMPage, EmployeePage and etc.)

├── tests/ # Tests

│ ├── conftest.py # fixtures, hooks, screenshots on failure
│ └── ... # e2e and negative tests

├── utils/ # helper functions (data generation, etc.)

├── requirements.txt

└── README.md
```


## ⚙️ Configuration
All settings are stored in `config/settings.py`:
```python
BASE_URL = "https://opensource-demo.orangehrmlive.com/"

VALID_USERNAME = "Admin"

VALID_PASSWORD = "admin123"

BROWSER = "chrome" 

HEADLESS = False
```
Installation and execution:

```
Clone and navigate:

git clone https://github.com/twelviieeeeeeee/orangeHRM_testovoe.git
cd orangeHRM_testovoe
```
```
Install dependencies:

pip install -r requirements.txt
```
```
Run all tests with HTML report:

pytest --html=report.html --self-contained-html
```
Screenshots on failures are saved automatically in tests/screenshots/ автоматически.

Test Coverage

11 tests implemented:
```
Positive:

Valid login

Navigate to PIM and create employee

Search employee by name

Edit employee profile

Check success messages, masks, and required fields

Logout
```
```
Negative:

Invalid login

Create employee without required fields

Search for a non-existent employee

Check save/cancel changes
```
Also, several login tests according to the requirements.
```
Artifacts

HTML-reports (report.html)

Screenshots on failure: tests/screenshots/
```
Author: Diana Muhortova

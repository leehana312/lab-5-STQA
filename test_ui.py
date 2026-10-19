"""Lab 5: automate login, create a task, mark it complete, log out.

Run with:
    pytest test_ui.py -v --html=report.html --self-contained-html
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.task_page import NewTaskPage, TaskListPage

DEMO_USERNAME = "demo"
DEMO_PASSWORD = "demo1234"
LOGOUT_LINK = (By.ID, "logout-link")


def test_login_with_valid_credentials(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(DEMO_USERNAME, DEMO_PASSWORD)

    # The new-task form only appears after a successful login.
    title_input = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(NewTaskPage.TITLE_INPUT)
    )
    assert title_input.is_displayed()
    assert "/login" not in driver.current_url


def test_login_with_invalid_credentials(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login("demo", "wrong-password")
    error = login_page.wait_for_error()
    assert "Invalid username or password" in error.text


def test_create_task(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(DEMO_USERNAME, DEMO_PASSWORD)

    new_task_page = NewTaskPage(driver, base_url)
    new_task_page.open()
    new_task_page.create_task(
        title="Prepare slides", priority="2", due_date="2026-12-01", hours="3"
    )
    banner = new_task_page.wait_for_success()
    assert banner.is_displayed()


def test_mark_task_complete_and_logout(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(DEMO_USERNAME, DEMO_PASSWORD)

    new_task_page = NewTaskPage(driver, base_url)
    new_task_page.open()
    new_task_page.create_task(
        title="Review report", priority="1", due_date="2026-12-05", hours="2"
    )
    new_task_page.wait_for_success()

    task_list_page = TaskListPage(driver, base_url)
    task_list_page.open()

    task_list_page.mark_complete(1)
    status = task_list_page.wait_until_completed(1)
    assert "Completed" in status.text

    driver.find_element(*LOGOUT_LINK).click()
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(LoginPage.USERNAME_INPUT)
    )
    assert "/login" in driver.current_url
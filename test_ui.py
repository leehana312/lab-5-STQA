"""Lab 5: automate login, create a task, mark it complete, log out.

Fill in pages/task_page.py first (it has TODO markers), then write the
four test functions below.

Run with:
    pytest test_ui.py -v --html=report.html --self-contained-html

DEMO_USERNAME = "demo"
DEMO_PASSWORD = "demo1234"
"""
from pages.login_page import LoginPage
from pages.task_page import NewTaskPage, TaskListPage

DEMO_USERNAME = "demo"
DEMO_PASSWORD = "demo1234"


def test_login_with_valid_credentials(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(DEMO_USERNAME, DEMO_PASSWORD)
    # TODO: wait for something on the next page that proves login
    # worked (the new-task form, or the page title). Assert on it.


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

    # TODO: use NewTaskPage to create a task with:
    #   title="Prepare slides", priority="2",
    #   due_date="2026-12-01", hours="3"
    # TODO: wait for the success banner and assert it is shown


def test_mark_task_complete_and_logout(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.open()
    login_page.login(DEMO_USERNAME, DEMO_PASSWORD)

    new_task_page = NewTaskPage(driver, base_url)
    # TODO: create a task here first, so there is something to complete

    task_list_page = TaskListPage(driver, base_url)
    task_list_page.open()

    # TODO: mark task 1 complete, then wait until its status cell
    # shows "Completed". Do not use time.sleep to wait for this.

    # TODO: click the logout link (id="logout-link") and confirm you
    # land back on the login page.

"""Page Objects for the task creation page and the task list page.

TODO: this file is incomplete. Fill in the methods marked TODO.
Use the LoginPage class in login_page.py as your pattern.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewTaskPage:
    TITLE_INPUT = (By.ID, "title")
    PRIORITY_INPUT = (By.ID, "priority")
    DUE_DATE_INPUT = (By.ID, "due_date")
    HOURS_INPUT = (By.ID, "hours")
    CREATE_BUTTON = (By.ID, "create-button")
    SUCCESS_BANNER = (By.ID, "success-banner")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url + "/")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TITLE_INPUT)
        )

    def create_task(self, title, priority, due_date, hours):
        # TODO: find each input by its locator above and call send_keys
        # TODO: click the create button
        pass

    def wait_for_success(self):
        # TODO: use WebDriverWait with expected_conditions to wait for
        # SUCCESS_BANNER to become visible. Do not use time.sleep.
        pass


class TaskListPage:
    TASK_TABLE = (By.ID, "task-table")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    @staticmethod
    def complete_button(task_id):
        return (By.CSS_SELECTOR, f'button[data-task-id="{task_id}"]')

    @staticmethod
    def status_cell(task_id):
        return (By.ID, f"status-{task_id}")

    def open(self):
        self.driver.get(self.base_url + "/tasks")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.TASK_TABLE)
        )

    def mark_complete(self, task_id):
        # TODO: find the complete_button(task_id) locator and click it.
        # This triggers a JavaScript call that takes about 0.7 seconds
        # to finish. Do NOT use time.sleep(1) to wait for it.
        pass

    def wait_until_completed(self, task_id):
        # TODO: use WebDriverWait with
        # expected_conditions.text_to_be_present_in_element to wait
        # until status_cell(task_id) contains the text "Completed".
        pass

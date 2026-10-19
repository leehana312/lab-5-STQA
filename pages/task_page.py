"""Page Objects for the task creation page and the task list page."""
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

    def _fill(self, locator, value):
        field = self.driver.find_element(*locator)
        if field.get_attribute("type") == "date":
            # Typing into a Chrome date picker depends on the locale
            # (mm/dd/yyyy vs yyyy-mm-dd). Setting the value directly
            # with the ISO format avoids that problem.
            self.driver.execute_script(
                "arguments[0].value = arguments[1];"
                "arguments[0].dispatchEvent(new Event('input', {bubbles: true}));"
                "arguments[0].dispatchEvent(new Event('change', {bubbles: true}));",
                field,
                value,
            )
        else:
            field.clear()
            field.send_keys(value)

    def create_task(self, title, priority, due_date, hours):
        self._fill(self.TITLE_INPUT, title)
        self._fill(self.PRIORITY_INPUT, priority)
        self._fill(self.DUE_DATE_INPUT, due_date)
        self._fill(self.HOURS_INPUT, hours)
        self.driver.find_element(*self.CREATE_BUTTON).click()

    def wait_for_success(self):
        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.SUCCESS_BANNER)
        )


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
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.complete_button(task_id))
        )
        button.click()

    def wait_until_completed(self, task_id):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.status_cell(task_id), "Completed")
        )
        return self.driver.find_element(*self.status_cell(task_id))
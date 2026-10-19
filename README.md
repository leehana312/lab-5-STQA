# Lab 5: Web UI Automation (Selenium)

**Duration:** 2 hours  **Work mode:** groups

**Application under test:** `https://pytodo-lab5.onrender.com` (a running PyTodo app with login)

## 1. What you are building

A Selenium script that opens a real browser, logs in, creates a task,
marks it complete, and logs out. No clicking by hand. The script does it.

## 2. Setup, step by step

**Step 1. Install Google Chrome**, if it is not already on your computer.
Download from google.com/chrome and install normally.

**Step 2. Install Python packages.** Open a terminal in this folder and run:

```bash
pip install -r requirements.txt
```

This installs `selenium`, `pytest`, and `pytest-html`. You do not need to
install a separate chromedriver file. Selenium 4.6 and later finds and
downloads the matching driver for your installed Chrome automatically, the
first time you run a test.

**Step 3. Confirm it works.** Run:

```bash
python -c "from selenium import webdriver; d = webdriver.Chrome(); d.get('https://example.com'); print(d.title); d.quit()"
```

A Chrome window should briefly open, visit example.com, and close. The
terminal should print `Example Domain`. If this fails, fix it before
continuing, nothing else in this lab will work until this line succeeds.

**Step 4. Set the app URL.** This repo's tests read the app address from
an environment variable. Set it once per terminal session:

```bash
export PYTODO_URL="https://pytodo-lab5.onrender.com"
```

On Windows PowerShell, use `$env:PYTODO_URL="https://pytodo-lab5.onrender.com"` instead.

**Step 5. Log in once by hand first.** Open `https://pytodo-lab5.onrender.com/login` in your own
browser, and check that logging in with username `demo` and password
`demo1234` works, and that you can create a task. This confirms the app
itself is reachable before you automate it.

## 3. Files in this repository

| File | Purpose |
|---|---|
| `pages/login_page.py` | Finished example. Read this first, it is your pattern. |
| `pages/task_page.py` | Has TODO markers. You complete this. |
| `test_ui.py` | Has TODO markers. You complete this. |
| `conftest.py` | Already complete. Opens and closes the browser for each test, takes a screenshot after every test. |

## 4. What is a Page Object, in one paragraph

Instead of writing raw Selenium commands inside every test, you write one
class per page. The class holds where things are on that page (the
locators) and what you can do on that page (the methods). A test then
reads as a short story: open the login page, log in, create a task. If
the web page changes later, only the Page Object file changes. The tests
stay the same.

## 5. The rule for this lab: no time.sleep

A page does not always finish loading or updating the instant you click
something. Marking a task complete on this app takes about 0.7 seconds
to process, through a background JavaScript call. If your test uses
`time.sleep(1)` to wait for it, two things can go wrong: it is slower
than necessary when 0.7 seconds would do, and it can still fail if the
server is briefly slower than your guessed number.

The correct tool is `WebDriverWait`, already used in `login_page.py`:

```python
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "some-id"))
)
```

This waits up to 10 seconds, checking repeatedly, and moves on the
instant the condition is true. Do not write `time.sleep` anywhere in
`pages/task_page.py` or `test_ui.py`.

## 6. Your task

1. Open `pages/login_page.py` and read it fully. This is a complete,
   working example.
2. Open `pages/task_page.py`. Fill in every method marked `TODO`,
   following the same pattern as `login_page.py`.
3. Open `test_ui.py`. Fill in every section marked `TODO`.
4. Run your tests:

```bash
pytest test_ui.py -v --html=report.html --self-contained-html
```

5. Open `report.html` in a browser. Every test should show a screenshot.
   A passing test's last screenshot should show the completed state
   (success banner shown, or task marked Completed). A failing test's
   screenshot shows you where it broke.

## 7. Submit

Commit `pages/task_page.py`, `test_ui.py`, and `report.html` to your repo.

| Criterion | Points |
|---|---|
| Login test (valid and invalid credentials) | 20 |
| Create task test, waits for success banner correctly | 20 |
| Mark complete test, uses WebDriverWait, not time.sleep | 25 |
| Logout test, confirms return to login page | 15 |
| HTML report generated with screenshots for every test | 20 |

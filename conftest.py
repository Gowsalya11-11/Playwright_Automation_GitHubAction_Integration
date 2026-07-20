import os
import pytest
from playwright.sync_api import sync_playwright
from utils.config_reader import ConfigReader

config = ConfigReader.read_config()

config = ConfigReader.read_config()
print("LOADED CONFIG:", config)

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser_name = config["browser"]

        if browser_name == "chromium":
            browser = p.chromium.launch(headless=config["headless"])
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=config["headless"])
        else:
            browser = p.webkit.launch(headless=config["headless"])

        yield browser

        browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(
        base_url=config.get("base_url"),
        record_video_dir="reports/videos/" if config.get("record_video") else None,
    )
    context.set_default_timeout(config.get("timeout", 5000))

    yield context

    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


# ---------- Auto screenshot on test failure ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\nScreenshot saved: {screenshot_path}")
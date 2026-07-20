from playwright.sync_api import Page, expect
import logging

logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.default_timeout = 5000  # ms

    # ---------- Navigation ----------
    def goto(self, url):
        self.page.goto(url)

    def get_current_url(self):
        return self.page.url

    def reload(self):
        self.page.reload()

    # ---------- Core Actions ----------
    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def type_text(self, locator, value, delay=50):
        """Types with delay, useful for triggering JS keyup/keydown events"""
        self.page.locator(locator).type(value, delay=delay)

    def clear(self, locator):
        self.page.locator(locator).fill("")

    def select_dropdown(self, locator, value):
        self.page.locator(locator).select_option(value)

    def check_checkbox(self, locator):
        self.page.locator(locator).check()

    def uncheck_checkbox(self, locator):
        self.page.locator(locator).uncheck()

    def hover(self, locator):
        self.page.locator(locator).hover()

    # ---------- Getters ----------
    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def get_all_texts(self, locator):
        return self.page.locator(locator).all_text_contents()

    def get_attribute(self, locator, attribute):
        return self.page.locator(locator).get_attribute(attribute)

    def get_input_value(self, locator):
        return self.page.locator(locator).input_value()

    def get_count(self, locator):
        return self.page.locator(locator).count()

    # ---------- State Checks ----------
    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def is_enabled(self, locator):
        return self.page.locator(locator).is_enabled()

    def is_checked(self, locator):
        return self.page.locator(locator).is_checked()

    # ---------- Waits ----------
    def wait_for_visible(self, locator, timeout=None):
        self.page.locator(locator).wait_for(
            state="visible", timeout=timeout or self.default_timeout
        )

    def wait_for_hidden(self, locator, timeout=None):
        self.page.locator(locator).wait_for(
            state="hidden", timeout=timeout or self.default_timeout
        )

    def wait_for_url(self, url_pattern, timeout=None):
        self.page.wait_for_url(url_pattern, timeout=timeout or self.default_timeout)

    def wait_for_load_state(self, state="load"):
        self.page.wait_for_load_state(state)

    # ---------- Assertions (built on Playwright's expect) ----------
    def assert_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def assert_text(self, locator, expected_text):
        expect(self.page.locator(locator)).to_have_text(expected_text)

    def assert_url(self, expected_url):
        expect(self.page).to_have_url(expected_url)

    # ---------- Debug / Utility ----------
    def screenshot(self, name="screenshot.png"):
        self.page.screenshot(path=f"reports/screenshots/{name}")

    def scroll_into_view(self, locator):
        self.page.locator(locator).scroll_into_view_if_needed()

    def log_action(self, message):
        logger.info(message)
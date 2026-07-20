import pytest
from pages.login_page import LoginPage
from utils.data_reader import DataReader


class TestLogin:

    def test_valid_login(self, page):
        login_page = LoginPage(page)
        user = DataReader.get("valid_user")

        login_page.open()
        login_page.login(user["username"], user["password"])

        assert "inventory.html" in login_page.get_current_url()

    def test_invalid_login(self, page):
        login_page = LoginPage(page)
        user = DataReader.get("invalid_user")

        login_page.open()
        login_page.login(user["username"], user["password"])

        error_text = login_page.get_error_message()
        assert "do not match" in error_text.lower()

    def test_locked_user_login(self, page):
        login_page = LoginPage(page)
        user = DataReader.get("locked_user")

        login_page.open()
        login_page.login(user["username"], user["password"])

        error_text = login_page.get_error_message()
        assert "locked out" in error_text.lower()
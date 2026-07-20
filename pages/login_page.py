from playwright.sync_api import Page
from locators.login_locators import Loginlocators
from pages.base_page import BasePage
from utils.config_reader import ConfigReader


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = Loginlocators.USERNAME
        self.password_input = Loginlocators.PASSWORD
        self.login_button = Loginlocators.LOGIN_BUTTON
        self.error_message = Loginlocators.ERROR_MESSAGE

        config = ConfigReader.read_config()
        self.base_url = config["base_url"]

    def open(self):
        self.page.goto(self.base_url)

    def enter_username(self,username):
        self.fill(self.username_input,username)

    def enter_password(self, password):
        self.fill(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.error_message)
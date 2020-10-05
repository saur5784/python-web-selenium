"""
the page object for the login screen.
"""

from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from utils.readconfig import get_config

BASE_URL = get_config()["base_url"]
UNAME = get_config()["username"]
PASSWD = get_config()["password"]


class LoginPage(BasePage):
    # locators for the page
    PAGE_HEADER = (By.XPATH, "//div[@class='p-refreshed_page__heading']")
    PAGE_SUB_HEADER = (By.XPATH, "//div[@class='p-refreshed_page__sub_heading']")
    EMAIL_INPUT = (By.ID, 'email')
    PWD_INPUT = (By.ID, 'password')
    SIGN_IN_BUTTON = (By.ID, 'signin_btn')

    # methods that operate on the locators

    def load(self):
        """
        load the current page
        """
        self.browser.get(BASE_URL)

    def log_in(self, username=UNAME, pswd=PASSWD):
        """
        log in to slack with pre-configured username and password or with overridden values
        :param username:
        :param pswd:
        """
        self.enter_text(self.EMAIL_INPUT, username)
        self.enter_text(self.PWD_INPUT, pswd)
        self.click(self.SIGN_IN_BUTTON)

    # asserts for the page

    def is_page_loaded(self):
        self.assert_element_text(self.PAGE_SUB_HEADER, BASE_URL.split('//')[1])
        return True

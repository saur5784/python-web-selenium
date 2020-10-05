"""
the page object for the send message panel.
"""

from pages.basepage import BasePage
from selenium.webdriver.common.by import By


class SendMessagePage(BasePage):
    # locators for the page
    MESSAGE_INPUT = (By.XPATH, "//div[@class='ql-editor ql-blank']")
    SEND_BUTTON = (By.XPATH, "//button[@data-qa='texty_send_button']")

    # methods that operate on the locators

    def enter_message(self, text):
        """
        enter text message into the message panel
        :param text:
        """
        self.enter_text(self.MESSAGE_INPUT, text)

    def tap_send_message_button(self):
        self.click(self.SEND_BUTTON)

    # asserts for the page

    def is_send_button_enabled(self):
        return self.is_enabled(self.SEND_BUTTON)

    def is_page_loaded(self):
        return self.is_clickable(self.MESSAGE_INPUT)

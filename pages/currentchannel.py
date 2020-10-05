"""
the page objects for current channel : MessagingPane and MoreActions
"""

from pages.basepage import BasePage
from selenium.webdriver.common.by import By


class MessagingPanePage(BasePage):
    # locators for the page
    MESSAGE_TEXT = (By.XPATH, '//div[text()="{}" and @class="p-rich_text_section"]')
    SEND_BUTTON = (By.XPATH, "//button[@data-qa='texty_send_button']")

    # methods that operate on the locators
    def hover_on_message(self, message):
        self.hover_to([self.MESSAGE_TEXT[0], self.MESSAGE_TEXT[1].format(message)])

    # asserts for the page
    def is_page_loaded(self, message):
        return self.is_visible([self.MESSAGE_TEXT[0], self.MESSAGE_TEXT[1].format(message)])


class MoreActionsPage(BasePage):
    # locators for the page
    ACTIONS_BUTTON = (By.XPATH, "//button[@data-qa='more_message_actions']")
    SAVE_BUTTON = (By.XPATH, "//button[@data-qa='save_message']")

    # methods that operate on the locators
    def click_on_save_button(self):
        if self.is_clickable(self.SAVE_BUTTON):
            self.click(self.SAVE_BUTTON)
        else:
            self.click(self.ACTIONS_BUTTON)
            self.click(self.SAVE_BUTTON)

    # asserts for the page
    def is_page_loaded(self):
        return self.is_clickable(self.ACTIONS_BUTTON)

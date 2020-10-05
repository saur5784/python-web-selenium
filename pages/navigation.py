"""
the page object for the top navigation panel : TopNavigation, ChannelSideBar and SaveItems
"""
from pages.basepage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TopNavigationPage(BasePage):
    # locators for the page
    SEARCH_BAR = (By.XPATH, "//button[@data-qa='top_nav_search']")
    SEARCH_INPUT = (By.XPATH, "//div[@class='ql-editor ql-blank' and @aria-label='Search']")
    SEARCH_RESULT = (By.XPATH, "//div[text()='{}']/ancestor::div[@data-qa='search_result']")
    CLOSE_BUTTON = (By.XPATH, "//button[@data-qa='search_input_close']")
    CLEAR_BUTTON = (By.XPATH, "//button[@data-qa='search_input_clear']")

    # methods that operate on the locators
    def click_on_search_bar(self):
        self.click(self.SEARCH_BAR)

    def clear_search_and_enter(self, message):
        if self.is_visible(self.CLEAR_BUTTON):
            self.click(self.CLEAR_BUTTON)
        self.enter_text(self.SEARCH_INPUT, message + Keys.ENTER)

    def click_on_close_button(self):
        self.click(self.CLOSE_BUTTON)

    # asserts for the page
    def is_page_loaded(self):
        return self.is_visible(self.SEARCH_BAR)

    def is_message_displayed_for_search_critera(self, message, criteria, retry=2):
        tries = 0
        while tries < retry:
            if self.is_visible([self.SEARCH_RESULT[0], self.SEARCH_RESULT[1].format(message)]):
                return True
            else:
                self.clear_search_and_enter(criteria)
                tries = tries + 1
        return False


class ChannelSideBarPage(BasePage):
    # locators for the page
    CHANNEL_NAV = (By.XPATH, "//nav[@data-qa-channel-sidebar='true']")
    SAVED_ITEMS = (By.XPATH, "//span[@data-qa='channel_sidebar_name_page_psaved']")

    # methods that operate on the locators
    def click_on_saved_items(self):
        self.click(self.SAVED_ITEMS)

    # asserts for the page
    def is_page_loaded(self):
        return self.is_visible(self.CHANNEL_NAV)


class SavedItemsPage(BasePage):
    # locators for the page
    PANE_TITLE = (By.XPATH, "//div[contains(text(),'Saved items')]/ancestor::div[@data-qa='saved_flexpane']")
    SAVED_ITEM = (By.XPATH, '//div[text()="{}" '
                            'and @class="p-rich_text_section"]/ancestor::div[@data-qa="saved_flexpane"]')

    # methods that operate on the locators

    # asserts for the page
    def is_page_loaded(self):
        return self.is_visible(self.PANE_TITLE)

    def is_message_displayed_in_saved_items(self, message):
        return self.is_visible([self.SAVED_ITEM[0], self.SAVED_ITEM[1].format(message)])

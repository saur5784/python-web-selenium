"""
base page object
"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def click(self, by_locator):
        """
        clicks on web element whose locator is passed to it.
        :param by_locator:
        """
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def assert_element_text(self, by_locator, element_text):
        """
        asserts comparison of a web element's text with passed in text.
        :param by_locator:
        :param element_text:
        """
        web_element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    def enter_text(self, by_locator, text):
        """
        enters the text in a web element whose locator is passed to it.
        :param by_locator:
        :param text:
        """
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_enabled(self, by_locator):
        """
        checks if the web element whose locator has been passed to it, is enabled or not and returns
        web element if it is enabled.
        :param by_locator:
        :return: True or False
        """
        try:
            return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            return False

    def is_visible(self, by_locator):
        """
        checks if the web element whose locator has been passed to it, is visible or not and returns
        true or false depending upon its visibility.
        :param by_locator:
        :return: True or False
        """
        try:
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except TimeoutException:
            return False

    def is_clickable(self, by_locator):
        """
        checks if the web element whose locator has been passed to it, is clickable or not and returns
        true or false depending upon its state.
        :param by_locator:
        :return: True or False
        """
        try:
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(by_locator))
            return bool(element)
        except TimeoutException:
            return False

    def hover_to(self, by_locator):
        """
        moves the mouse pointer over a web element whose locator has been passed to it.
        :param by_locator:
        """
        element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.browser).move_to_element(element).perform()

"""
This module contains web test cases for starring a message.
"""

import random

from pages.login import LoginPage
from pages.sendmessage import SendMessagePage
from pages.currentchannel import MessagingPanePage, MoreActionsPage
from pages.navigation import TopNavigationPage, ChannelSideBarPage, SavedItemsPage


def test_star_message(browser):
    search_criteria = "has:star"
    bot_message = "Hello, I am bot{}".format(random.randint(0, 100))

    # launch and log in to slack web client
    login_page = LoginPage(browser)
    login_page.load()
    assert login_page.is_page_loaded(), "Login page did not load"
    login_page.log_in()

    # send a message in the current channel
    send_message = SendMessagePage(browser)
    assert send_message.is_page_loaded(), "SendMessage panel did not load"
    send_message.enter_message(bot_message)
    assert send_message.is_send_button_enabled(), "Send Message button is not enabled"
    send_message.tap_send_message_button()

    # load actions view and save/star message
    message_pane = MessagingPanePage(browser)
    assert message_pane.is_page_loaded(bot_message), "{} was not found in the message pane".format(bot_message)
    message_pane.hover_on_message(bot_message)
    actions = MoreActionsPage(browser)
    assert actions.is_page_loaded(), "More Actions page was not loaded"
    actions.click_on_save_button()

    # launch search nav bar and assert message found as starred
    search = TopNavigationPage(browser)
    assert search.is_page_loaded(), "Top nav search page was not loaded"
    search.click_on_search_bar()
    search.clear_search_and_enter(search_criteria)
    assert search.is_message_displayed_for_search_critera(bot_message, search_criteria), \
        "{} is not displayed in search{} results".format(bot_message, search_criteria)
    search.click_on_close_button()

    # launch saved items and assert message found
    side_bar = ChannelSideBarPage(browser)
    assert side_bar.is_page_loaded(), "Channel Side bar was not loaded"
    side_bar.click_on_saved_items()

    saved_items = SavedItemsPage(browser)
    assert saved_items.is_page_loaded(), "Saved Items pane was not loaded"
    assert saved_items.is_message_displayed_in_saved_items(bot_message), \
        "{} was not found in the Saved Items pane".format(bot_message)

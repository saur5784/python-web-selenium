"""
This module contains shared fixtures for UI tests.
"""
import pytest

from os.path import dirname, join
from selenium.webdriver import Chrome
from utils.readconfig import get_config

project_root = dirname(dirname(__file__))
DRIVERS_PATH = join(project_root, 'resources/drivers')
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome']


@pytest.fixture(scope='session')
def config():
    return get_config()


@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture
def browser(config_browser, config_wait_time):
    # Initialize WebDriver
    if config_browser == 'chrome':
        driver = Chrome(executable_path=DRIVERS_PATH + '/chromedriver')
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()

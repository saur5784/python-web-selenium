"""
utility to read config.json
"""

import json
from os.path import dirname, join

project_root = dirname(dirname(__file__))
CONFIG_PATH = join(project_root, 'resources/config.json')


def get_config():
    """
    Read the JSON config file and returns it as a parsed dict
    :return: json object with config data
    """
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data

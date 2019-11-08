#!/usr/bin/env python3

import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read("config.txt")
    url = config.get("configuration", "URL")
    token = config.get("configuration", "token")
    config = {'url': url, 'token': token}
    return (config)

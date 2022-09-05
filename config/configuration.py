import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '', 'config.ini'))


class Configuration:
    @staticmethod
    def get_url():
        url = config.get("login", "baseurl")
        return url

    @staticmethod
    def get_username():
        username = config.get("login", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("login", "password")
        return password

from configparser import ConfigParser
import os


class ConfigReader(object):

    @staticmethod
    def get_value(section, key):
        config = ConfigParser()
        config.read('/Users/abhishek/PycharmProjects/mweb-iOS/headout.ini')
        return config[section][key]

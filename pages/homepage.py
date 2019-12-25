import time
from locators.homepage_locators import homepage_locators
from locators.svg_locators import svg_locators


class homepage(object):

    def __init__(self, webdriver):
        self.driver = webdriver

    def click_search_bar(self, url):
        time.sleep(10)
        self.driver.find_element(*homepage_locators.search_bar).click()
        time.sleep(5)
        self.driver.find_element(*homepage_locators.search_bar).send_keys(url)
        time.sleep(10)
        self.driver.find_element(*homepage_locators.search_bar).send_keys('\n')
        time.sleep(20)
        # self.driver.find_element(*homepage_locators.collections_icon).click()
        # time.sleep(5)
        # self.driver.find_element(*homepage_locators.account_icon).click()
        # time.sleep(5)
        # self.driver.find_element(*homepage_locators.explore_icon).click()
        # time.sleep(5)
        # self.driver.find_element(*homepage_locators.search_bar).click()
        # time.sleep(5)
        # self.driver.find_element(*homepage_locators.search_bar).send_keys(url)
        # time.sleep(10)
        # self.driver.find_element(*homepage_locators.search_bar).send_keys('\n')
        # time.sleep(20)

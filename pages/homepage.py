from Utilities.DriverManager import AppTestAppium
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from selenium import webdriver
from seleniumpagefactory import Pagefactory
from locators.homepage_locators import homepage_locators
import time

class homepage(object):

    def __init__(self, webdriver):
        self.driver = webdriver

    def click_search_bar(self):
        time.sleep(10)
        self.driver.find_element(*homepage_locators.search_bar).click()
        self.driver.find_element(*homepage_locators.search_bar).send_keys('malani')


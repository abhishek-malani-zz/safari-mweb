from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from Utilities.DriverManager import AppTestAppium
from locators.homepage_locators import homepage_locators
from pages.homepage import homepage

import time

def main():
    driver = AppTestAppium.instantiate_driver()
    time.sleep(10)
    elements = homepage(driver).click_search_bar()


if __name__ == '__main__':
    main()

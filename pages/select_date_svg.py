import time
from locators.svg_locators import svg_locators


class select_date_svg(object):

    def __init__(self, webdriver):
        self.driver = webdriver

    def select_date(self):
        self.driver.find_element(*svg_locators.next_btn).click()
        time.sleep(10)
        self.driver.find_element(*svg_locators.lets_go_btn).click()
        self.driver.find_elements(*svg_locators.available_date)

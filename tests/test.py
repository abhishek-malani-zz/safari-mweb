import time

from Utilities.ConfigReader import ConfigReader
from Utilities.DriverManager import AppTestAppium
from pages.homepage import homepage
from pages.select_date_svg import select_date_svg


def main():
    driver = AppTestAppium.instantiate_driver()
    time.sleep(10)
    driver.get('https://www.headout.com/book/7563')
    time.sleep(5)
    homepage(driver).click_search_bar(ConfigReader.get_value('ENVIRONMENT', 'test_url'))
    select_date_svg(driver).select_date()


if __name__ == '__main__':
    main()

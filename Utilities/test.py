from Utilities.DriverManager import AppTestAppium

x = AppTestAppium()


def main():
    driver = x.instantiate_driver()
    driver.find_element_by_name('Address')
    driver.find_element_by_name('Address').clear()
    driver.find_element_by_name('Address').send_keys('hello')


if __name__ == '__main__':
    main()

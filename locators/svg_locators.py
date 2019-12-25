from appium.webdriver.common.mobileby import MobileBy


class svg_locators(object):
    back_btn = (MobileBy.CLASS_NAME, 'close-button-wrapper')
    tour_info = (MobileBy.CLASS_NAME, 'booking-flow-header-title notranslate')
    help_icon = (MobileBy.CLASS_NAME, 'header-chat-button')
    month_list = (MobileBy.CLASS_NAME, 'date-picker-big')
    month_title = (MobileBy.CLASS_NAME, 'month-title')
    day_list = (MobileBy.CLASS_NAME, 'day-list')
    date_list = (MobileBy.CLASS_NAME, 'date-list')
    #available_date = (MobileBy.CLASS_NAME, 'date-big-wrapper ')
    available_date = (MobileBy.XPATH, "(//div[@class='date-list']/div[@class='date-big-wrapper   '])[1]")
    lets_go_btn = (MobileBy.CLASS_NAME, 'book-now available')
    next_btn = (MobileBy.CLASS_NAME, "core-button core-primary-button call-to-action call-to-action-button ")



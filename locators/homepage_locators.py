from appium.webdriver.common.mobileby import MobileBy


class homepage_locators(object):
    search_bar = (MobileBy.ACCESSIBILITY_ID, 'URL')
    search_icon = (MobileBy.CLASS_NAME, 'header-search-icon')
    headout_logo = (MobileBy.CLASS_NAME, 'logo-image-wrapper ')
    explore_icon = (MobileBy.CLASS_NAME, 'tile block feed-tab active-tab')
    collections_icon = (MobileBy.CLASS_NAME, 'tile block collections-tab')
    account_icon = (MobileBy.CLASS_NAME, 'tile block account-tab')
    bannner_image = (MobileBy.CLASS_NAME, 'banner-image visible')
    search_field = (MobileBy.CLASS_NAME, 'search-input-wrapper ')
    category_icons = (MobileBy.CLASS_NAME, 'circular-categories-wrapper clearfix')
    top_experiences_header = (MobileBy.CLASS_NAME, 'heading')

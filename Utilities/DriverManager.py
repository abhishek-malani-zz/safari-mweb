from appium import webdriver


class AppTestAppium:
    @staticmethod
    def instantiate_driver():
        desired_caps = {'platformName': 'iOS',
                        'platformVersion': '12.4',
                        'deviceName': 'iPhone XR',
                        'automationName': 'xcuitest',
                        'bundleId': 'com.apple.mobilesafari',
                        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return driver

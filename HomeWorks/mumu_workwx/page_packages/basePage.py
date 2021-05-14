from appium import webdriver

from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, _driver: WebDriver = None):
        if _driver is None:

            caps = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": True,
                "dontStopAppOnReset": 'true',
                "skipDeviceInitialization": 'true'
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)

        else:
            self.driver = _driver

    def find_ele(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        return self.find_ele(by, locator).click()

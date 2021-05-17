# 启动app ，重启， 关闭
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from HomeWorks.test_appium.pages.base_page import BasePage
from HomeWorks.test_appium.pages.main_page import MainPage


class App(BasePage):

    def start(self):

        if self.driver == None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"] = True
            print("初始化 driver")
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            print("复用driver")
            # 启动 desired capabilities 设置过的 app
            self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        # 关闭
        self.driver.close()
        # 启动app
        self.driver.launch_app()

    def goto_main(self) -> MainPage:
        # 箭头指定返回的数据类型
        return MainPage(self.driver)

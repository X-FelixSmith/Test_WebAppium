from appium.webdriver.common.mobileby import MobileBy

from HomeWorks.test_appium.pages.base_page import BasePage
from HomeWorks.test_appium.pages.contact_page import ContactPage

# 首页
class MainPage(BasePage):
    def goto_contact(self):
        # 点击通讯录 进入通讯录页面
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录']")
        return ContactPage(self.driver)

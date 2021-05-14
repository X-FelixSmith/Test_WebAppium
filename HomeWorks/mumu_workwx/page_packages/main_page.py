from appium.webdriver.common.mobileby import MobileBy

from HomeWorks.mumu_workwx.page_packages.basePage import BasePage
from HomeWorks.mumu_workwx.page_packages.contacts_page import ContactsPage


# 首页
class MainPage(BasePage):

    # 到通讯录页面
    def goto_Contacts(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录']")
        return ContactsPage(self.driver)

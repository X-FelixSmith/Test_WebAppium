from appium.webdriver.common.mobileby import MobileBy

from HomeWorks.mumu_workwx.page_packages.addMember_page import AddMemberPage
from HomeWorks.mumu_workwx.page_packages.basePage import BasePage


# 通讯录页面
class ContactsPage(BasePage):

    # 点击添加成员 进入到 添加成员页面
    def click_addmember(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='添加成员']")
        return AddMemberPage(self.driver)

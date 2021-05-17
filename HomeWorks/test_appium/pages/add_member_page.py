# 添加成员页
from appium.webdriver.common.mobileby import MobileBy

from HomeWorks.test_appium.pages.base_page import BasePage


class AddMemberPage(BasePage):

    def click_addmember_manually(self):
        # 点击 手动输入
        from HomeWorks.test_appium.pages.edit_member_page import EditMemberPage

        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return EditMemberPage(self.driver)

    def verify_toast(self):
        self.find_ele(MobileBy.XPATH, "//*[@text='添加成功']")
        return True

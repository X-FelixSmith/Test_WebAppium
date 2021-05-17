
# 个人信息设置页
from appium.webdriver.common.mobileby import MobileBy

from HomeWorks.test_appium.pages.base_page import BasePage
from HomeWorks.test_appium.pages.edit_member_complete_page import EditMemberCompletePage


class EditPersonInfoPage(BasePage):
    def click_edit_member(self):
        # 点击编辑成员
        self.find_and_click(MobileBy.XPATH, "//*[@text='编辑成员']")
        return EditMemberCompletePage(self.driver)


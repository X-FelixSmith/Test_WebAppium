# 手动添加成员页
from appium.webdriver.common.mobileby import MobileBy

from HomeWorks.test_appium.pages.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phone_num):
        # 输入 姓名,
        # 输入 电话,
        # 点击保存
        from HomeWorks.test_appium.pages.add_member_page import AddMemberPage
        self.find_and_send_keys(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']", name)
        self.find_and_send_keys(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']", phone_num)
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

        return AddMemberPage(self.driver)

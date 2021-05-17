from appium.webdriver.common.mobileby import MobileBy

from HomeWorks.test_appium.pages.base_page import BasePage


# 个人信息页
class PersonInfoPage(BasePage):
    def goto_person_info_setting(self):
        # 点击 右上角三个点到 编辑个人信息页
        # self.find_and_click()
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/h8g")

        from HomeWorks.test_appium.pages.edit_personInfo_page import EditPersonInfoPage
        return EditPersonInfoPage(self.driver)

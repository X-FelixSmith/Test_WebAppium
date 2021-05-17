from appium.webdriver.common.mobileby import MobileBy

from HomeWorks.test_appium.pages.base_page import BasePage


# 编辑成员 完整信息页
class EditMemberCompletePage(BasePage):
    def click_delete_member(self):
        # 点击删除成员
        # 点击确定
        # 回到通讯录页面
        self.swipe_find('删除成员').click()
        self.find_and_click(MobileBy.XPATH, "//*[@text='确定']")

        from HomeWorks.test_appium.pages.contact_page import ContactPage
        return ContactPage(self.driver)

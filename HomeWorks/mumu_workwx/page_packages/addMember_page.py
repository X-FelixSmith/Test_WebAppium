from appium.webdriver.common.mobileby import MobileBy

from HomeWorks.mumu_workwx.page_packages.addMemberInfo_page import AddMemberInfo
from HomeWorks.mumu_workwx.page_packages.basePage import BasePage


# 添加成员页面
class AddMemberPage(BasePage):

    # 点击”手动输入添加“成员 到 添加成员信息页面
    def click_AddManually(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return AddMemberInfo(self.driver)

    # 点击返回到通讯录页面
    def backTo_Contacts(self):
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/h86")

        from HomeWorks.mumu_workwx.page_packages.contacts_page import ContactsPage
        return ContactsPage(self.driver)


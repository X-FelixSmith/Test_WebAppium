from appium.webdriver.common.mobileby import MobileBy

from HomeWorks.mumu_workwx.page_packages.basePage import BasePage


# 添加成员信息页面
class AddMemberInfo(BasePage):

    # 输入成员信息，并点击保存
    def add_member_info(self,name,phone):
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ays").send_keys(name)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f4m").send_keys(phone)
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

        # 返回toast 提示信息的文案
        toast_text = self.find_ele(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        # print(f"toast-text: ",toast_text)
        return toast_text

        # from HomeWorks.mumu_workwx.page_packages.addMember_page import AddMemberPage
        # return AddMemberPage(self.driver)

from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from HomeWorks.test_appium.pages.add_member_page import AddMemberPage

# 通讯录页
from HomeWorks.test_appium.pages.base_page import BasePage
from HomeWorks.test_appium.pages.personInfo_page import PersonInfoPage


# 通讯录页
class ContactPage(BasePage):

    def click_add_member(self):
        # 点击添加成员，跳转到添加成员页
        self.swipe_find('添加成员', 10).click()
        return AddMemberPage(self.driver)

    def find_member(self, text):
        # 按名字查找成员
        self.swipe_find(f"{text}", 5).click()
        return PersonInfoPage(self.driver)

    def confirm_del_member(self, text):
        sleep(2)
        # print("确认是否删除成功")
        ele = self.swipe_find(f"{text}", 1)

        return ele

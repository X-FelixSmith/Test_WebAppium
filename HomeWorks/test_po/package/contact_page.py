from time import sleep

from selenium.webdriver.common.by import By

from HomeWorks.test_po.package.add_member_page import AddMemberPage
from HomeWorks.test_po.package.basepage import BasePage


# 通讯录页面
class ContactPage(BasePage):
    # 点击添加成员
    def click_add_member(self):
        # 添加成员按钮需要确定一个进行点击，否则有几率报错
        while True:
            self.find_and_click(By.CSS_SELECTOR, ".ww_operationBar:nth-child(1)>.js_add_member")
            ele_num = len(self.finds(By.ID, "username"))
            if ele_num > 0:
                break
        return AddMemberPage(self.driver)

    # 得到成员信息
    def get_member(self):
        sleep(2)
        member_list = []
        ele_phones = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(5)")
        for value in ele_phones:
            member_list.append(value.get_attribute("title"))
        return member_list

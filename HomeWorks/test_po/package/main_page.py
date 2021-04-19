from selenium.webdriver.common.by import By

from HomeWorks.test_po.package.add_member_page import AddMemberPage
from HomeWorks.test_po.package.basepage import BasePage
from HomeWorks.test_po.package.contact_page import ContactPage


# 主页
class MainPage(BasePage):
    # 首页url
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 点击通讯录
    def goto_contact(self):
        self.find_and_click(By.ID, "menu_contacts")
        return ContactPage(self.driver)

    # 点击添加成员
    def click_add_member(self):
        self.find_and_click(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)")
        return AddMemberPage(self.driver)

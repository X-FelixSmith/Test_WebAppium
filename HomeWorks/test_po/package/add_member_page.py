from selenium.webdriver.common.by import By

from HomeWorks.test_po.package.basepage import BasePage


# 添加成员页面
class AddMemberPage(BasePage):

    # 添加成员信息并保存
    def add_member(self, name, gid, phone):
        # 避免循环导入，局部导入
        from HomeWorks.test_po.package.contact_page import ContactPage

        self.find(By.ID, "username").send_keys(name)
        self.find(By.ID, "memberAdd_acctid").send_keys(gid)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find_and_click(By.CSS_SELECTOR, ".js_btn_save")

        return ContactPage(self.driver)

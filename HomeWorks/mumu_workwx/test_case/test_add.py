import pytest
import yaml

from HomeWorks.mumu_workwx.page_packages.main_page import MainPage


class TestAddmember:
    with open("../datas/data_1.yaml") as f:
        datas = yaml.safe_load(f)

    def setup(self):
        self.main = MainPage()
        pass

    def teardown(self):
        self.main.driver.quit()

    # 冒烟测试：测试企业微信 手动输入添加成员功能
    @pytest.mark.parametrize("name,phone", datas["info"], ids=datas["ids"])
    def test_add(self, name, phone):
        msg = self.main.goto_Contacts().click_addmember().click_AddManually().add_member_info(name, phone)
        assert msg == "添加成功"

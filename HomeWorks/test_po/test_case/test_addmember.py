import pytest

from HomeWorks.test_po.package.main_page import MainPage

# 添加成员测试用例
class TestAddmember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    # 首页-通讯录-添加成员-通讯录断言
    @pytest.mark.parametrize("name,gid,phone", [("lisi", "0419001", "18800001000"), ("wangwu", "0419002", "18800002000")],
                             ids=["case1", "case2"])
    def test_addmember1(self, name, gid, phone):
        ele = self.main.goto_contact().click_add_member().add_member(name, gid, phone).get_member()
        print(ele)
        assert phone in ele

    # 首页-添加成员-通讯录断言
    @pytest.mark.parametrize("name,gid,phone", [("zhaoliu", "0419003", "18800003000"), ("mahan", "0419004", "18800004000")],
                             ids=["case3", "case4"])
    def test_addmember2(self, name, gid, phone):
        ele = self.main.click_add_member().add_member(name, gid, phone).get_member()
        assert phone in ele

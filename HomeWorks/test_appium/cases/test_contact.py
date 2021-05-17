import pytest
from faker import Faker
from selenium.common.exceptions import NoSuchElementException

from HomeWorks.test_appium.pages.app import App
from HomeWorks.test_appium.pages.base_page import BasePage


class TestContact:
    def setup_class(self):
        self.faker = Faker('zh_CN')
        self.app = App()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back()

    # 使用两条数据进行测试
    data = BasePage().get_datas(3)

    @pytest.mark.parametrize('name,phone_num', data[0], ids=data[1])
    def test_add_member(self, name, phone_num):
        # 测试用例: 添加成员
        result = self.main.goto_contact().click_add_member(). \
            click_addmember_manually().edit_member(name, phone_num).verify_toast()
        assert result

    @pytest.mark.parametrize('name', data[2], ids=data[1])
    def test_del_member(self, name):
        # 测试用例: 删除成员
        try:
            ele = self.main.goto_contact().find_member(name).goto_person_info_setting(). \
                click_edit_member().click_delete_member().confirm_del_member(name)
            assert ele is None
        except NoSuchElementException as e:
            assert e.msg == 0

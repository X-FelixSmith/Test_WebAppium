import allure

from HomeWorks.test_requests.apis.tag import Tag
from HomeWorks.test_requests.test_cases.utils import Utils


@allure.feature("标签管理测试")
class TestTag:

    def setup_class(self):
        # 获取通讯录对应的token
        conf_data = Utils.get_yaml_data("../data/conf.yaml")
        corp_id = conf_data["corpid"]["mywork"]
        corp_secret = conf_data["secret"]["contact_secret"]
        # 实例化标签类
        self.tag = Tag(corp_id, corp_secret)
        # 清除标签数据
        self.tag.clear_tags()
        # 测试数据
        self.tag_id = 16
        self.create_data = {
            "tagname": "TEST",
            "tagid": self.tag_id
        }
        self.update_data = {
            "tagname": "TEST_update",
            "tagid": self.tag_id
        }

    @allure.story("标签场景测试用例")
    def test_tag_scene(self):
        # 创建标签
        with allure.step("创建标签"):
            self.tag.create_tag(self.create_data)
        # 查询是否创建成功
        with allure.step("查询标签创建结果"):
            tag_info = self.tag.get_tag_list()
            print(tag_info)
            tagid_list = Utils.base_jsonpath(tag_info, "$..tagname")
            self.tag.log_info(tagid_list)
            assert "TEST" in tagid_list

        # 更新标签
        with allure.step("更新标签"):
            self.tag.update_tag(self.update_data)
        with allure.step("查询标签更新结果"):
            tag_info = self.tag.get_tag_list()
            name_list = Utils.base_jsonpath(tag_info, "$..tagname")
            self.tag.log_info(name_list)
            assert "TEST_update" in name_list

        # 删除标签
        with allure.step("删除标签"):
            self.tag.delete_tag(self.tag_id)
        with allure.step("查询标签删除结果"):
            tag_info = self.tag.get_tag_list()
            if len(tag_info["taglist"]) > 0:
                tag_id_list = Utils.base_jsonpath(tag_info, "$..tagid")
                self.tag.log_info(tag_id_list)
                assert self.tag_id not in tag_id_list

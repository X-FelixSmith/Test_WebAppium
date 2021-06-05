import pytest
import requests


class TestTag:

    def setup_class(self):
        corpid = "wwf9941b46c51c399e"
        corpsecret = "WrHORWp_Pw0j9O1_Qdy0av1P7diImwNOmWw9L_QDbi8"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.request("get", url=url)

        self.token = r.json()["access_token"]
        self.tagid = 15

    @pytest.mark.parametrize("tagname, expect", [
        ("Test1", 0),
        ("Test2", 0),
        ("Test3", 0)
    ])
    def test_create_tag(self, tagname, expect):
        '''
        创建 tag标签
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        data = {
            "tagname": tagname,
        }
        r = requests.request("POST", url, json=data)
        print(r.json())
        assert r.json()['errcode'] == expect

    def test_update_tag(self):
        '''
        更新标签
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        data = {
            "tagname": "Test_update",
            "tagid": self.tagid
        }
        r = requests.request("POST", url, json=data)
        # print(r.json())
        assert r.json()['errcode'] == 0

    def test_get_tag(self):
        """
        查询标签
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={self.tagid}"
        r = requests.request("get", url)
        print(r.json())
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize("tagid, expect", [
        (1, 0), (2, 0), (3, 0)
    ])
    def test_delete_tag(self, tagid, expect):
        """
        删除标签
        :param tagid: 标签id
        :param expect: 期望值
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}"
        r = requests.request("GET", url)
        assert r.json()['errcode'] == expect

    def test_get_tag_list(self):
        '''
        获取标签列表
        :return: 返回标签列表接口响应
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        r = requests.request("get", url)
        return r.json()

    def test_clear_tag(self):
        '''
        清空标签
        '''
        tag_list_info = self.test_get_tag_list()
        tag_list = tag_list_info["taglist"]
        if len(tag_list) > 0:
            for i in tag_list:
                self.test_delete_tag(i["tagid"], 0)

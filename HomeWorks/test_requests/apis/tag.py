from HomeWorks.test_requests.apis.wework import WeWork


class Tag(WeWork):

    def create_tag(self, data):
        '''
        创建标签
        :param data: body 数据
        :return: 创建标签接口响应
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        req = {
            "method": "post",
            "url": url,
            "json": data
        }
        r = self.req_res(req)
        return r.json()

    def update_tag(self, data):
        '''
        更新标签
        :param data:
        :return: 更新标签接口响应
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        req = {
            "method": "post",
            "url": url,
            "json": data
        }
        r = self.req_res(req)
        return r.json()

    def get_tag_member(self, tag_id):
        '''
        获取标签成员
        :param tag_id:
        :return:获取标签成员接口响应结果
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tag_id}"

        req = {
            "method": "get",
            "url": url
        }
        r = self.req_res(req)
        return r.json()

    def delete_tag(self, tag_id):
        '''
        删除标签
        :param tag_id:
        :return:删除标签接口响应结果
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tag_id}"
        req = {
            "method": "get",
            "url": url
        }
        r = self.req_res(req)
        return r.json()

    def get_tag_list(self):
        '''
        获取标签列表
        :return:获取标签列表接口响应结果
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        req = {
            "method": "get",
            "url": url
        }
        r = self.req_res(req)
        return r.json()

    def clear_tags(self):
        '''
        清理标签
        '''
        tag_list = self.get_tag_list()["taglist"]
        if len(tag_list) > 0:
            for i in tag_list:
                self.delete_tag(i["tagid"])

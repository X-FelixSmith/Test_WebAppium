from HomeWorks.test_requests.apis.base_api import BaseApi


class WeWork(BaseApi):
    def __init__(self, corpid, corpsecret):
        self.token = self.get_token(corpid, corpsecret)

    def get_token(self, corpid, corpsecret):
        '''
        获取 access_token
        :param corpid: id
        :param corpsecret: secret
        :return: access_token
        '''
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        r = self.req_res(req)
        token = r.json()["access_token"]
        return token

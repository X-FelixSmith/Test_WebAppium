import logging

import requests


class BaseApi:
    # 设置 loging
    fileHandler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    logging.getLogger().setLevel(0)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    fileHandler.setFormatter(formatter)
    logging.getLogger().addHandler(fileHandler)

    def req_res(self, req):
        '''
        对 requests进行封装
        :param req:字典格式的参数
        :return:接口响应结果
        '''
        self.log_info("----requests data----")
        self.log_info(req)
        r = requests.request(**req)
        self.log_info("----response data----")
        self.log_info(r.json())
        return r

    def log_info(self, msg):
        '''
        添加日志信息
        :param msg: 日志信息
        :return:返回 info 级别的日志
        '''
        return logging.info(msg)

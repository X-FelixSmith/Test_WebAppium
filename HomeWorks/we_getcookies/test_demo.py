'''
    课后作业：使用序列化的方法用cookie登录企业微信
'''
from time import sleep

import yaml
from selenium import webdriver


class TestWe:

    # 复用浏览器获得cookie 保存在yaml中
    def test_getcookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        cookies = driver.get_cookies()

        with open("data_cookies.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookies, f)

    # 获取已有cookies 加入driver 可免扫码登录
    def test_login(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(6)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")

        with open("./data_cookies.yaml", encoding="UTF-8") as f:
            cookies = yaml.safe_load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)

        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(2)

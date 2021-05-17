import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from faker import Faker
from selenium.common.exceptions import NoSuchElementException


# 基类 存放最基本的方法
class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, _driver: WebDriver = None):
        self.driver = _driver

    # 滚动查找
    def swipe_find(self, text, num=3):
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:
                ele = self.find_ele(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return ele
            except:
                # print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get('height')
                start_x = width / 2
                start_y = height * 4 / 5
                end_x = width / 2
                end_y = height * 1 / 5

                self.driver.swipe(start_x, start_y, end_x, end_y)
            if i == (num - 1):
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(0)

    def find_ele(self, by, locator):
        logging.info('find')
        logging.info(by)
        logging.info(locator)
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        logging.info('find_and_click')
        return self.find_ele(by, locator).click()

    def find_and_send_keys(self, by, locator, text):
        return self.find_ele(by, locator).send_keys(text)

    def back(self, num=4):
        for i in range(num):
            self.driver.back()

    def get_datas(self, num=3):
        fake = Faker('zh-CN')
        data_s = []
        data_name = []
        ids = []
        data = []
        for i in range(num):
            name = fake.name()
            data.append((name, fake.phone_number()))
            ids.append(f"case {i + 1}")
            data_name.append(name)
        data_s.append(data)
        data_s.append(ids)
        data_s.append(data_name)
        return data_s

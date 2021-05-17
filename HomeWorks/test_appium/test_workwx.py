from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class TestWorkWx:
    def setup_class(self):
        self.fake = Faker('zh_CN')

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["ensureWebviewsHavePages"] = True
        caps['settings[waitForIdleTimeout]'] = 0
        caps["dontStopAppOnReset"] = 'true'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def swipe_find(self, text, num=3):
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:
                ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return ele
            except:
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get('height')
                start_x = width / 2
                start_y = height * 4 / 5
                end_x = width / 2
                end_y = height * 1 / 5

                self.driver.swipe(start_x, start_y, end_x, end_y)
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException()

    def test_demo(self):
        print(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='通讯录']")(self.driver))

    def test_work_wx(self):

        name = self.fake.name()
        phonenum = self.fake.phone_number()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.swipe_find(text="添加成员").click()
        # WebDriverWait(self.driver, 5).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']"))
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # WebDriverWait(self.driver, 5).until(
        #     lambda x: x.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']"))
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")

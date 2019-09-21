import time

from appium import webdriver


class TestSetting:

    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "8.1.0",
            "deviceName": "12",  # device_name android中可以随便写，iOS中不可以
            # app信息 包名和启动名
            "appPackage": "com.android.settings",
            "appActivity": ".Settings",
            "unicodeKeyboard":True,
            "resetKeyboard":True,
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)

    def teardown(self):
        self.driver.close_app()

    def test_mobiles_network_2g(self):
        # print("这是2g")
        self.driver.find_element_by_xpath("//*[contains(@text,'Network & Internet')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'Mobile network')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'Advanced')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'Preferred network type')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

    def test_mobiles_network_3g(self):
        self.driver.find_element_by_xpath("//*[contains(@text,'Network & Internet')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'Mobile network')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'Advanced')]").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'Preferred network type')]").click()
        # time.sleep(3)
        self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()

    def test_display_search(self):
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys("hello")
from appium import webdriver

import os, sys
# 解决自己创建的模块在命令行无法找到的问题
sys.path.append(os.getcwd())

from base.base_driver import init_driver

from page.display_page import DisplayPage

class TestDisplay():

    def setup(self):

       self.driver = init_driver()
       self.display_page = DisplayPage(self.driver)

    def teardown(self):
        self.driver.close_app()
        self.driver.quit()

    def test_display_search(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.driver.find_element_by_class_name("android.widget.EditText").send_keys("hello")
        self.display_page.click_image()
        self.display_page.input_search_text("hello")
        self.display_page.click_back()
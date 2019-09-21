from appium import webdriver
import os, sys

sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.network_page import NetWorkPage


class TestNetwork():

    def setup(self):
        self.driver = init_driver()
        self.network_page = NetWorkPage(self.driver)
    def teardown(self):
        self.driver.close_app()
        self.driver.quit()

    def test_mobiles_network_2g(self):
        self.network_page.click_network()
        self.network_page.click_mobile()
        self.network_page.click_advanced()
        self.network_page.click_preferred()
        self.network_page.click_2g()





    def test_mobiles_network_3g(self):
        self.network_page.click_network()
        self.network_page.click_mobile()
        self.network_page.click_advanced()
        self.network_page.click_preferred()
        self.network_page.click_3g()
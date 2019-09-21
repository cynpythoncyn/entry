
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class NetWorkPage(BaseAction):
    # 定义按钮变量
    network_button = By.XPATH,"//*[contains(@text,'Network & Internet')]"
    mobile_button = By.XPATH,"//*[contains(@text,'Mobile network')]"
    advanced_button = By.XPATH,"//*[contains(@text,'Advanced')]"
    preferred_button = By.XPATH,"//*[contains(@text,'Preferred network type')]"
    network_2g_button = By.XPATH,"//*[contains(@text,'2G')]"
    network_3g_button = By.XPATH,"//*[contains(@text,'3G')]"

    def __init__(self,driver):
        BaseAction.__init__(self,driver)


    def click_network(self):
        # self.find_element(self.network_button).click()
        self.click(self.network_button)
    def click_mobile(self):
        # self.find_element(self.mobile_button).click()
        self.click(self.mobile_button)
    def click_advanced(self):
        # self.find_element(self.advanced_button).click()
        self.click(self.advanced_button)
    def click_preferred(self):
        # self.find_element(self.preferred_button).click()
        self.click(self.preferred_button)
    def click_2g(self):
        # self.find_element(self.network_2g_button).click()
        self.click(self.network_2g_button)

    def click_3g(self):
        # self.find_element(self.network_3g_button).click()
        self.click(self.network_3g_button)




from selenium.webdriver.support.wait import WebDriverWait


class BaseAction():
    """
    1.脚本（scripts）注重的是操作的执行的先后顺序
    2.特征是页面提供的
    3.base action 是根据page的特征去做操作（比如：click，send_keys，input_text等）
    """

    def __init__(self,driver):
        self.driver = driver

    def find_element(self,loc,time=10,poll=1):
        by = loc[0]
        value = loc[1]
        return WebDriverWait(self.driver,time,poll).until(lambda x:x.find_element(by,value))

    def find_elements(self,loc,time=10,poll=1):
        by = loc[0]
        value = loc[1]
        return WebDriverWait(self.driver,time,poll).until(lambda x:x.find_elements(by,value))

    def click(self,loc):
        self.find_element(loc).click()

    def input_text(self,loc,text):
        self.find_element(loc).send_keys(text)
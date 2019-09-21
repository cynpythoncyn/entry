from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class DisplayPage(BaseAction):

    image_button = By.CLASS_NAME,"android.widget.ImageButton"
    edittext_button = By.CLASS_NAME,"android.widget.EditText"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    def click_image(self):
        # self.find_element(self.image_button).click()
        self.click(self.image_button)
    def input_search_text(self,text):


        # self.find_element(self.edittext_button).send_keys("hello")
        self.input_text(self.edittext_button,text)
    def click_back(self):
        # self.find_element(self.back_button).click()
        self.click(self.back_button)
    # def find_element(self,loc):
    #     return self.driver.find_element(loc[0],loc[1])
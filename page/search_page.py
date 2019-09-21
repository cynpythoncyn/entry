from selenium.webdriver.common.by import By

from base.base_action import BaseAction

class SearchPage(BaseAction):

    image_button = By.CLASS_NAME, "android.widget.ImageButton"
    edittext_button = By.CLASS_NAME, "android.widget.EditText"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self,driver):

        # BaseAction.__init__(self,driver)
        super(SearchPage, self).__init__(driver)

    def click_image(self):
        self.click(self.image_button)

    def input_search_text(self,text):
        self.input_text(self.edittext_button,text)

    def click_back(self):

        self.click(self.back_button)


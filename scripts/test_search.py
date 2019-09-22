import os, sys, pytest

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.search_page import SearchPage
from base.read_data import ReadData


class TestSearch():

    def setup(self):
        self.driver = init_driver()
        self.search_page = SearchPage(self.driver)

    def teardown(self):
        self.driver.close_app()
        self.driver.quit()

    @pytest.mark.parametrize("test_id,input_text",ReadData("search_data.yaml").return_search_data("test_search", "search_001"))
    def test_search(self, test_id, input_text):
        self.search_page.click_image()
        self.search_page.input_search_text(input_text)
        self.search_page.click_back()
        assert 0

    @pytest.mark.parametrize("test_id,input_text",ReadData("search_data.yaml").return_search_data("test_search1", "search_002"))
    def test_search1(self, test_id, input_text):
        self.search_page.click_image()
        self.search_page.input_search_text(input_text)
        self.search_page.click_back()

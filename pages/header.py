from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    Search_input = (By.ID, 'twotabsearchtextbox')
    Search_button = (By.ID, 'nav-search-submit-button')

    def search_product(self):
        self.input_text('coffee', *self.Search_input)

    def click_search(self):
        self.click(*self.Search_button)
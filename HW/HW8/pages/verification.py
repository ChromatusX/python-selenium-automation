from HW.HW8.pages.base_page import Page
from selenium.webdriver.common.by import By


class Verification(Page):

    department = (By.CSS_SELECTOR, '#nav-subnav[data-category="books"]')

    def verify_department(self):
        self.wait_for_element_appear(*self.department)
from HW.HW7.pages.header import Header
from HW.HW7.pages.main_page import MainPage
from HW.HW7.pages.verification import Verification


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.verification = Verification(self.driver)


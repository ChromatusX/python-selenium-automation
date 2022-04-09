from HW.HW8.pages.header import Header
from HW.HW8.pages.main_page import MainPage
from HW.HW8.pages.verification import Verification


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.verification = Verification(self.driver)


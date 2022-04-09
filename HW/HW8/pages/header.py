from HW.HW8.pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Header(Page):

    Select_Department = (By.ID, 'searchDropdownBox')
    Search_bar = (By.ID, 'twotabsearchtextbox')
    NEW_ARRIVAL = (By.CSS_SELECTOR, "a[href*='/New-Arrivals']")
    Arrival_menu = (By.XPATH, "//div[@class='mega-menu']")

    def select_department(self):
        select_department = self.driver.find_element(*self.Select_Department)
        select = Select(select_department)
        select.select_by_value('search-alias=stripbooks')

    def search_item(self):
        search = self.driver.find_element(*self.Search_bar)
        search.send_keys("games")
        search.send_keys(Keys.RETURN)

    def hover_new_arrival(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*self.NEW_ARRIVAL))
        actions.perform()

    def verify_arrival_menu(self):
        self.wait_for_element_appear(*self.Arrival_menu)
from HW.HW7.pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):

    Orders_button = (By.ID, 'nav-orders')
    Cart_button = (By.ID, 'nav-cart-count-container')

    def click_orders_button(self):
        self.click(*self.Orders_button)

    def click_cart_button(self):
        self.click(*self.Cart_button)

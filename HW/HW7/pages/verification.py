from HW.HW7.pages.base_page import Page
from selenium.webdriver.common.by import By


class Verification(Page):
    sign_in_page = (By.XPATH, "//*[@class='a-spacing-small']")
    cart_result = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")

    def verify_sign_in_page(self, expected_result):
        actual_result = self.driver.find_element(*self.sign_in_page).text
        assert expected_result == actual_result, f"Expected text {expected_result} but got {actual_result}"

    def verify_empty_cart(self, expected_result):
        actual_result = self.driver.find_element(*self.cart_result).text
        assert expected_result == actual_result, f"Expected  {expected_result} but got {actual_result}"

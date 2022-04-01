from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon home page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Click on returns and orders')
def click_returns_orders(context):
    context.app.header.click_orders_button()


@then('Verify {expected_result} page')
def verify_found_results_text(context, expected_result):
    context.app.verification.verify_sign_in_page(expected_result)
    print("Test case 1 pass")


@when('Click cart button')
def click_cart_button(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()


@then('Verify if empty cart message')
def verify_empty_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    context.app.verification.verify_empty_cart(expected_result)
    print("Test case 2 pass")



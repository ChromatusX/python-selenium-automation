from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon Home Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click cart button')
def click_cart_button(context):
    context.driver.find_element(By.ID, 'nav-cart-count-container').click()
    sleep(1)


@then('Verify if empty cart message')
def verify_empty_cart(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2").text
    expected_result = 'Your Amazon Cart is empty'

    print(f"The result is {actual_result}")

    assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"
    print('Test case passed')
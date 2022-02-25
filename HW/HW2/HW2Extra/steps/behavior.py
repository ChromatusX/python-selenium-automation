from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Amazon home page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')



@when('Click on returns and orders')
def click_returns_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

    sleep(1)


@then('Verify Sign in page')
def verify_found_results_text(context):
    actual_result = context.driver.find_element(By.XPATH, "//*[@class='a-spacing-small']").text
    expected_result = 'Sign-In'

    print(actual_result)

    assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"
    print('Test case passed')
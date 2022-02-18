from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys


@given('Open Amazon help page')
def open_google(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Search for Cancel order')
def click_search_icon(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel Order')
    context.driver.find_element(By.ID, 'helpsearch').send_keys(Keys.RETURN)
    sleep(1)

@then('Verify if help page')
def verify_found_results_text(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
    expected_result = 'Cancel Items or Orders'

    print(f"The result is {actual_result}")

    assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"
    print('Test case passed')
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input {item} on search bar')
def search_item(context, item):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(f"{item}")


@then('Click the search button')
def click_search_button(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').send_keys(Keys.RETURN)


@then('Click on first item to add')
def click_on_first_item(context):
    context.driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]").click()


@then('Add item to cart')
def add_item_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()
    sleep(5)


@then('Verify item in cart')
def verify_item_in_cart(context):
    amount = context.driver.find_element(By.ID, 'nav-cart-count').text
    convertamount = int(amount)
    print(type(convertamount))
    print(f"Cart has {convertamount} item(s)")
    expected_result = 1
    assert expected_result == convertamount, f'Expected {expected_result}, but got {convertamount}'
    print("Test case passed")
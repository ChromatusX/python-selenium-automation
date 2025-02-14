from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given("Open Amazon T&C page")
def open_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when("Store original window")
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@then("Click on Amazon Privacy Notice link")
def click_privacy_link(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/privacy']").click()


@when("Switch to new window")
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print('\nCurrent:', current_windows)
    context.driver.switch_to.window(current_windows[1])


@then("Verify Amazon Privacy Notice page is opened")
def verify_amazon_privacy_page(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'))


@then("User can close new window and switch back to original")
def close_new_switch_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
    current_windows = context.driver.window_handles
    print('\nCurrent:', current_windows)






from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys


@given('Open Amazon bestseller page')
def open_amazon_bestseller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Check for links')
def check_links(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq li")
    print(links)
    print(len(links))
    expected_result = 5

    assert len(links) == expected_result, f'Expected {expected_result} links but got {len(links)}'
    print('Test case passed')
    sleep(1)


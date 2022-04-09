from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon home page')
def open_amazon(context):
    context.app.main_page.open_main()


@when('Select books department')
def select_department(context):
    context.app.header.select_department()


@when('Search for game')
def search_item(context):
    context.app.header.search_item()


@then('Verify books department is selected')
def verify_department(context):
    context.app.verification.verify_department()


@given('Open item page')
def open_item_page(context):
    context.app.main_page.open_url('/gp/product/B074TBCSC8')


@when('Hover over arrival')
def hover_new_arrival(context):
    context.app.header.hover_new_arrival()
    sleep(2)


@then('Verify new arrival details')
def verify_new_arrival(context):
    context.app.header.verify_arrival_menu()
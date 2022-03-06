from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


Color_selection = (By.CSS_SELECTOR, "#variation_color_name li")
Current_color = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given("Open the item page")
def open_page(context):
    context.driver.get("https://www.amazon.com/gp/product/B07BJL37GD/?th=1")


@then("Verify clicking all the color options")
def color_check(context):
    colors = context.driver.find_elements(*Color_selection)
    expect_colors = ['Black', 'Dark Blue Vintage', 'Dark Indigo/Rinsed', 'Dark Wash', 'Indigo Wash', 'Light Blue Vintage', 'Light Wash', 'Medium Blue, Vintage', 'Medium Wash', 'Rinsed', 'Vintage Wash', 'Washed Black', 'Bright White', 'Dark Khaki Brown', 'Light Khaki Brown', 'Olive', 'Sage Green', 'Blue, Over Dye', 'Blue, Dip Dye']
    #list_of_colors = []
  #  for color in colors:
  #      color.click()
  #      current_color = context.driver.find_element(*Current_color).text
  #      list_of_colors += [current_color]
  #  actual_amount = len(list_of_colors)
  #  print(list_of_colors)

  #  assert expect_amount == len(list_of_colors), f'Actual amount {actual_amount} do not match {expect_amount}'

    for i in range(len(colors)):
        print('item:', i)
        colors[i].click()
        current_color = context.driver.find_element(*Current_color).text
        print('current color: ', current_color)
        print('expected color:', expect_colors[i])
        assert current_color == expect_colors[i], f'Actual color is {current_color}, expected {expect_colors[i]}'

        print('Test case passed')




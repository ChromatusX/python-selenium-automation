from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# init driver
driver = webdriver.Chrome(executable_path =r'C:\Users\hongl\OneDrive\Desktop\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get("https://www.amazon.com/gp/help/customer/display.html")

sleep(2)
search = driver.find_element(By.ID, 'helpsearch')
search.clear()
search.send_keys('Cancel order')
search.send_keys(Keys.RETURN)

sleep(2)
actual_result = driver.find_element(By.XPATH, "//*[text()='Cancel Items or Orders']").text
expected_result = 'Cancel Items or Orders'

print(actual_result)

assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"
print('Test case passed')
driver.quit()









from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path =r'C:\Users\hongl\OneDrive\Desktop\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

driver.get('https://www.amazon.com')

#search_filed = driver.find_element(By.ID, 'twotabsearchtextbox')
#search_filed.send_keys('coffee')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('game')
driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"game"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
print(actual_result)

assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"
print('Test case passed')
driver.quit()
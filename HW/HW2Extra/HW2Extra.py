from selenium import webdriver
from selenium.webdriver.common.by import By


# init driver
driver = webdriver.Chrome(executable_path =r'/chromedriver.exe')
driver.maximize_window()

# open the url
driver.get("https://www.amazon.com")

driver.find_element(By.ID, 'nav-orders').click()

actual_result = driver.find_element(By.XPATH, "//*[@class='a-spacing-small']").text
expected_result = 'Sign-In'

print(actual_result)

assert expected_result == actual_result, f"Expected text {expected_result} did not match {actual_result}"
print('Test case passed')
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path =r'C:\Users\hongl\OneDrive\Desktop\python-selenium-automation\chromedriver.exe')
driver.maximize_window()

driver.get("https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&prevRID=4AY884S9E6HNY3H9YYEH&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

#amazon logo
driver.find_element(By.CSS_SELECTOR, "[href='/ref=ap_frn_logo']")

#creat account logo

driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

#Your name

driver.find_element(By.ID, "ap_customer_name")

#Email

driver.find_element(By.ID, "ap_email")

#Password

driver.find_element(By.ID, "ap_password")

#Password must be atleast 6 characters

driver.find_element(By.CSS_SELECTOR, ".auth-inlined-information-message .a-alert-content")


#Re-enter password

driver.find_element(By.ID, "ap_password_check")

#Continue button

driver.find_element(By.ID, "continue")

#Condtions of use

driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='ap_register_notification_condition']")

#Privacy notice

driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='ap_register_notification_privacy']")


#Sign in if have account

driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?']")


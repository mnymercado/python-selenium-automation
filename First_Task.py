from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


service = Service('/Users/nicolemercado/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

#1st Task

driver.find_element(By.ID, "nav-orders").click()
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']") # Amazon Logo
driver.find_element(By.ID, "ap_email").send_keys('Hello') # Email Field
driver.find_element(By.ID, "continue") # Continue Field
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click() # Need Help Link
driver.find_element(By.ID, "auth-fpp-link-bottom") # Forgot Password Link
driver.find_element(By.ID, "ap-other-signin-issues-link") # Other issues with Sign-In link
driver.find_element(By.ID, "createAccountSubmit") # Create your Amazon account button
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']") # Conditions of use link
driver.find_element(By.XPATH, "//a[@href= '/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']") # Privacy Notice link

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[text()]").text
assert expected_result == actual_result, f'Expected result is {expected_result} but result is {actual_result}'
print("Test Passed")

sleep(5)
driver.quit()

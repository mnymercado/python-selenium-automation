from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


service = Service('/Users/nicolemercado/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

sleep(5)

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('phone')
driver.find_element(By.ID, 'nav-search-submit-button').click()


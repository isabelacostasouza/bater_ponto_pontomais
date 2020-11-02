import time
from selenium import webdriver

email = '[your_email]'
password = '[your_password]'

driver = webdriver.Chrome()
driver.get('https://app.pontomaisweb.com.br/#/acessar')

emailElement = driver.find_element_by_name("login")
emailElement.send_keys(email)

passwordElement = driver.find_element_by_name("password")
passwordElement.send_keys(password)

submitLoginElement = driver.find_element_by_class_name("btn-primary")
submitLoginElement.click()

driver.implicitly_wait(100)

submitMarkElement = driver.find_element_by_xpath('//button[text()="Registrar ponto"]')
submitMarkElement.click()

time.sleep(2)

driver.close()

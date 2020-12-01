from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("http://amazon.com")
print(driver.title)

driver.get("http://ebay.com")
print(driver.title)

driver.back()

print(driver.title)

driver.forward()

print(driver.title)


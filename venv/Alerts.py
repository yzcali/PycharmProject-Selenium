from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

time.sleep(3)

#driver.switch_to.alert.accept()  # You pressed OK!
driver.switch_to.alert.dismiss() #You pressed Cancel!
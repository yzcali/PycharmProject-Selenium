from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
element = driver.find_element_by_id("tinymce")
element.clear()
element.send_keys("anlasildi tmm geldik")

driver.switch_to.default_content()
driver.find_element_by_link_text("Elemental Selenium").click()
time.sleep(3.0)
driver.close()
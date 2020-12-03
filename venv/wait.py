from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome()
driver.get("http://fhctrip-qa.com/admin/HotelAdmin/Create")

driver.implicitly_wait(5)

driver.find_element_by_id("UserName").send_keys("manager2")
driver.find_element_by_id("Password").send_keys("Man1ager2!"+Keys.ENTER)
#print(driver.title)
assert "Admin - List Of Hotels" in driver.title






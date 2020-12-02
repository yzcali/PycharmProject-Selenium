from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://fhctrip-qa.com/admin/HotelAdmin/Create")
ele=driver.find_element_by_id("UserName")
print(ele.is_displayed())  # True
print(ele.is_enabled())    # True

ele1 = driver.find_element_by_id("Password")
print(ele1.is_displayed())   # True
print(ele1.is_enabled())     # True

ele.send_keys("manager2")
ele1.send_keys("Man1ager2!"+Keys.ENTER)

ele2 = driver.find_element_by_id("Code")
print(ele2.is_selected())  # False because it is not a radio button selector like roundtrip or oneway



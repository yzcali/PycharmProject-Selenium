from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.utils import Keys
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://fhctrip-qa.com/admin/HotelAdmin/Create")
driver.find_element_by_id("UserName").send_keys("manager2")
driver.find_element_by_id("Password").send_keys("Man1ager2!"+Keys.ENTER)
time.sleep(3.5)
driver.get("https://fhctrip-qa.com/admin/HotelAdmin")
rows= len(driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div/div[3]/div/div/div[2]/div/div/div[2]/table/thead/tr")) # count number of rows
cols= len(driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div/div[3]/div/div/div[2]/div/div/div[2]/table/thead/tr[1]/th"))  # count number of cols

print(rows)
print(cols)

for r in range(2,rows+1):
    for c in range(1,cols):
        value=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[3]/div/div/div[2]/div/div/div[2]/table/thead/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value)


driver.close()
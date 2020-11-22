from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:/Users/yzc/PycharmProjects/SeleniumProject/drivers/chromedriver.exe")
# driver = webdriver.Firefox("C:/Users/yzc/PycharmProjects/SeleniumProject/drivers/geckodriver.exe")
driver.maximize_window()
driver.set_page_load_timeout(10)

driver.get("http://amazon.com")
driver.find_element_by_id("twotabsearchtextbox").send_keys("Samsung" + Keys.ENTER)
driver.find_element_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']").click()
time.sleep(5)
driver.refresh()
time.sleep(3)
driver.close()

print("test completed successfully! ")

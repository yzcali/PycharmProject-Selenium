from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")

#1. yol
#driver.execute_script("window.scrollBy(0,8000)","")

#2. yol
#flag= driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div/div/div[62]/div/a/img")
#driver.execute_script("arguments(0).scrollIntoView();",flag)

#3.yol
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") # end of the page

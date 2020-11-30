from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome()
driver.get("https://amazon.com")

print(driver.title)
print(driver.current_url)

driver.find_element_by_id("twotabsearchtextbox").send_keys("pillowpet"+ Keys.ENTER)
driver.find_element_by_xpath("//img[@class='s-image']").click()


driver.close()
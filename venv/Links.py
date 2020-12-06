from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://ebay.com")

links = driver.find_elements(By.TAG_NAME,"a")
#1 ) how many links present in a page
print("Number of links present: " , len(links))  # Number of links present:  385

# note : to see for the list of links
#for link in links:
   # print(link.text)

#2 ) clicking on the link

driver.find_element(By.LINK_TEXT, "Registration").click()
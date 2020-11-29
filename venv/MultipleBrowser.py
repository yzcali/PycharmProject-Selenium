from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#driver= webdriver.Firefox()
driver.get("https://amazon.com")
print(driver.title)
 # Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more
print(driver.current_url)
# https://www.amazon.com/
print(driver.page_source) # <html lang="en-us" class=... goes on all codes of html .
driver.close()
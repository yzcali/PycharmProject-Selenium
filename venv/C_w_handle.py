from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.adidas.com")
driver.get("http://nike.com")
print(driver.current_window_handle) # CDwindow-A72334A17C990C3EF555EF70435C7F30
handles = driver.window_handles # return all the handle values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

driver.quit()
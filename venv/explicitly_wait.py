from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://www.skyscanner.fr/")

driver.find_element_by_xpath("//button").click()


driver.find_element_by_id("fsc-origin-search").send_keys("Paris (Tous)")
driver.find_element_by_id("fsc-destination-search").send_keys("New York, NY (Tous)")

driver.find_element_by_id("depart-fsc-datepicker-button").clear()
driver.find_element_by_id("depart-fsc-datepicker-button").send_keys("10/12/2020")

driver.find_element_by_id("return-fsc-datepicker-button").clear()
driver.find_element_by_id("return-fsc-datepicker-button").send_keys("17/12/2020")

driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div/div/div/div/div/form/div[3]/button").click()
# explicit waits
wait =WebDriverWait(driver,7)
element = wait.until(EC.element_to_be_clickable(driver.find_element_by_id("submitted")))
element.click()

time.sleep(3)

driver.quit()
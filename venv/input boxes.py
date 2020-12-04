from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
# how to find how many inputboxes present in web page

inputboxes=driver.find_elements(By.CLASS_NAME,'text_field')
print (len(inputboxes)) #6
# how to provide value into the text box
driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("alex")
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("Ferguson")
driver.find_element(By.ID, 'RESULT_TextField-3').send_keys("03562282301")
driver.find_element(By.ID, 'RESULT_TextField-4').send_keys("Germany")
driver.find_element(By.ID, 'RESULT_TextField-5').send_keys("koln")
driver.find_element(By.ID, 'RESULT_TextField-6').send_keys("alex@mail.com")



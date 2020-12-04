from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
# working with the radiobuttons

#status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
#print(status)

driver.find_element_by_xpath("//*[@id='RESULT_RadioButton-7_0']").click()
status1= driver.find_element_by_xpath("//*[@id='RESULT_RadioButton-7_0']").is_selected()
print(status1)
#working with check boxes

driver.find_element_by_id("RESULT_CheckBox-8_3").click()

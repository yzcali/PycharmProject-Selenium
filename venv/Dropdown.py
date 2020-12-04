from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
element =driver.find_element_by_id("RESULT_RadioButton-9")
drp=Select(element)
#select by index
#drp.select_by_index(1)
#select by visible text
#drp.select_by_visible_text("Morning")
#select by value
drp.select_by_value("Radio-0")

#Count number of the options
print(len(drp.options)) #4

#capture all the options and print them as output
all_options=drp.options

for option in all_options:
    print(option.text)
    # null , morning , Afternoon, Evening
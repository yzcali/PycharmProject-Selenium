from behave import *
from selenium import webdriver


@given(u'launch chrome browser')
def launchBrowser(context):
    # context.driver = webdriver.Chrome("C:/Users/yzc/PycharmProjects/SeleniumProject/drivers/chromedriver.exe")
    context.driver = webdriver.Chrome()


@when(u'open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")


@then(u'verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#num1")
    x = x_element.text
    x1 = int(x)
    y_element = browser.find_element_by_css_selector("#num2")
    y = y_element.text
    y1 = int(y)
    xy = int(x + y)
    xy = str (int(x1 + y1))

    #select = Select(browser.find_element_by_css_selector("#dropdown"))
    select = Select(browser.find_element_by_css_selector("select"))
    list1 = browser.find_element_by_css_selector("#dropdown")
    list1.click()
    list2 = select.select_by_value(xy)
    list2.click()
    
finally:
    list1.click()
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
    time.sleep(10)
    browser.quit()
    print (xy)


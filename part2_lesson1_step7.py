from selenium import webdriver
import math
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#treasure")
    x1 = x_element.get_attribute("valuex")

    def calc(x1):
        return str(math.log(abs(12*math.sin(int(x1)))))
    
    y = calc(x1)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    click1 = browser.find_element_by_css_selector('#robotCheckbox')
    click1.click()
    click2 = browser.find_element_by_css_selector('#robotsRule')
    click2.click()
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()
    
finally:
    time.sleep(30)
    browser.quit()

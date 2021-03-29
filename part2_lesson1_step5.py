from selenium import webdriver
import math
import time

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    click1 = browser.find_element_by_css_selector('#robotCheckbox')
    click1.click()
    click2 = browser.find_element_by_css_selector('#robotsRule')
    click2.click()
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()

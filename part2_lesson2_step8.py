from selenium import webdriver
import math
import time
import os 

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Лилуш")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Британский13")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("lilyshlanpirysh@gmail.com")
    file = browser.find_element_by_css_selector("[type='file']")
    #current_dir = os.path.abspath(os.path.dirname(__Secret__))    
    #file_path = os.path.join(current_dir, 'Secret.txt')            
    file.send_keys(os.getcwd() + "/Secret.txt")
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
    
finally:
    time.sleep(10)
    print("ok")
    browser.quit()

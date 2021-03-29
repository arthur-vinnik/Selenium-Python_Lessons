from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("#book")
    
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    x1 = int(x)
    def calc(x1):
        return str(math.log(abs(12*math.sin(int(x1)))))
    y = calc(x1)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()

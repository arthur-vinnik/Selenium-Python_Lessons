from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('input.form-control.first[required]')
    input1.send_keys("Ктун")
    input2 = browser.find_element_by_css_selector('input.form-control.second[required]')
    input2.send_keys("Древний")
    input3 = browser.find_element_by_css_selector('input.form-control.third[required]')
    input3.send_keys("C'Thun@gmail.com")
    input4 = browser.find_element_by_css_selector('.form-control.first:not(required)')
    input4.send_keys("+380888888888")
    input5 = browser.find_element_by_css_selector('div.second_block > div.form-group.second_class > input.form-control.second')
    input5.send_keys("Hidden in Azeroth")
    # Отправляем заполненную форму
    time.sleep(3)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

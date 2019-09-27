from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os
#
# link = 'http://suninjuly.github.io/selects1.html'
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     sum = str(int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text))
#     browser.find_element_by_tag_name("select").click()
#     select = Select(browser.find_element_by_tag_name("select"))
#     select.select_by_value(sum)
#     browser.find_element_by_css_selector('button.btn.btn-default').click()
#
# finally:
#     time.sleep(15)
#     browser.quit()

# browser = webdriver.Chrome()
# link = " http://SunInJuly.github.io/execute_script.html"
# browser.get(link)
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
#
# x_element = browser.find_element_by_id ('input_value')
# x = x_element.text
# y = calc(x)
# x_input = browser.find_element_by_id('answer')
# x_input.send_keys(y)
# check_1 = browser.find_element_by_id('robotCheckbox').click()
# radio_1 = browser.find_element_by_id('robotsRule')
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# radio_1.click()
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# button.click()



link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("admin@admin.ua")

    file = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    file.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
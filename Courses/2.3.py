from selenium import webdriver
import math
import time


# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser.get(link)
#     button = browser.find_element_by_css_selector("[type='submit']")
#     button.click()
#     confirm = browser.switch_to.alert
#     confirm.accept()
#
#     def calc(x):
#         return str(math.log(abs(12*math.sin(int(x)))))
#
#     element = browser.find_element_by_id("input_value").text
#     x = int(element)
#     y = calc(x)
#
#     input = browser.find_element_by_id("answer")
#     input.send_keys(y)
#     button = browser.find_element_by_css_selector("button.btn.btn-primary")
#     button.click()
#
# finally:
#     # успеваем скопи
#     time.sleep(30)
#     # закрываем брау
#     browser.quit()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)
time.sleep(10)
button = browser.find_element_by_css_selector("button.trollface")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

btn = browser.find_element_by_css_selector("button.btn")
btn.click()
# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# browser.implicitly_wait(5)
# browser.get("http://suninjuly.github.io/wait1.html")
#
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element_by_class_name("btn-primary")
button.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

btn = browser.find_element_by_id("solve")
btn.click()

browser.quit()


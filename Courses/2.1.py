from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#
#     def calc(x):
#         return str(math.log(abs(12 * math.sin(int(x)))))
#
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text
#
#     y = calc(x)
#
#     input1 = browser.find_element_by_id("answer")
#     input1.send_keys(y)
#
#     checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
#     radio = browser.find_element_by_css_selector("[for='robotsRule']").click()
#
#     button = browser.find_element_by_css_selector("[type='submit']")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


brow = webdriver.Chrome()
brow.get('http://suninjuly.github.io/get_attribute.html')

pic = brow.find_element_by_tag_name('img')
x = pic.get_attribute("valuex")
print(x)
print(type(x))
y = calc(x)

find = brow.find_element_by_css_selector('input')
find.send_keys(y)

check = brow.find_element_by_id('robotCheckbox')
check.click()

radio = brow.find_element_by_css_selector("[value='robots']")
radio.click()

button = brow.find_element_by_css_selector('button.btn')
button.click()
brow.quit()
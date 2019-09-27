from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
# link = "http://suninjuly.github.io/registration2.html"


browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys("Ivan")
#for registration2
#browser.find_element_by_css_selector('[placeholder="Input your name"]').send_keys("Ivan")

browser.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys("Petrov")
#need comment for registration2

browser.find_element_by_css_selector('[placeholder="Input your email"]').send_keys("admin@admin.ua")


time.sleep(10)
button = browser.find_element_by_xpath("//button[contains(text(), 'Submit')]")
button.click()
time.sleep(10)
browser.quit()

# не забываем оставить пустую строку в конце файла



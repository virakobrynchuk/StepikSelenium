from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder = 'Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("third")
    input3.send_keys("mail@mail.ru")

    button = browser.find_element_by_xpath("//button[text() ='Submit']")
    button.click()
       
    time.sleep(1)
    welcome_text_elt= browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 19:07:36 2019

@author: sokol
"""

from selenium import webdriver
import time


try: 
    browser = webdriver.Chrome()
    
    #path_chromedriver = r"C:\chromedriver"
    #browser = webdriver.Chrome(path_chromedriver+"\chromedriver.exe")
    
    link_ok = "http://suninjuly.github.io/registration1.html"
    link_er = "http://suninjuly.github.io/registration2.html"
    browser.get(link_er)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_css_selector(".first_block input.first").send_keys('My_first_name')
    browser.find_element_by_css_selector(".first_block input.second").send_keys('My_last_name')
    browser.find_element_by_css_selector(".first_block input.third").send_keys('My_E-mail@mail.ru')
    
    #насладиться заполнением формы
    time.sleep(5)
    
    # Отправляем заполненную форму
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
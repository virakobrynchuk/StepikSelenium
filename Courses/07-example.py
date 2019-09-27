from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    driver = webdriver.Chrome()
    driver.get(link)

    # Заполняем обязательные поля
    first_name = driver.find_element_by_css_selector("input[placeholder='Input your first name']")
    first_name.send_keys("Ivan")

    last_name = driver.find_element_by_css_selector("input[placeholder='Input your last name']")
    last_name.send_keys("Petrov")

    email = driver.find_element_by_css_selector("input[placeholder='Input your email']")
    email.send_keys("ivan.petrov@example.com")

    # Отправляем заполненную форму
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться, ждем загрузки страницы
    time.sleep(1)

    # Находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # Записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(3)
    driver.quit()

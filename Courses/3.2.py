from selenium import webdriver
import time
import unittest


class TestSelectors(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser = None

    def get_link(self, link):
        # link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        input1 = self.browser.find_element_by_css_selector(".first_block > .first_class > input.first")
        input1.send_keys("first name")
        input2 = self.browser.find_element_by_css_selector(".first_block > .second_class > input.second")
        input2.send_keys("surname")
        input3 = self.browser.find_element_by_css_selector(".first_block > .third_class > input.third")
        input3.send_keys("e-mail")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        return welcome_text

    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.get_link(link)

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.get_link(link)

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)


if __name__ == "__main__":
    unittest.main()
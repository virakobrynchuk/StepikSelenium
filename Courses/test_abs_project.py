import unittest

# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#     def test_abs2(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#
# if __name__ == "__main__":
#     unittest.main()


from selenium import webdriver
import time
import unittest


def test1():
    link1 = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link1)

    browser.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys("Ivan")

    browser.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys("Petrov")

    browser.find_element_by_css_selector('[placeholder="Input your email"]').send_keys("admin@admin.ua")

    button = browser.find_element_by_xpath("//button[contains(text(), 'Submit')]")
    button.click()


def test2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('[placeholder="Input your name"]').send_keys("Ivan")

    browser.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys("Petrov")

    browser.find_element_by_css_selector('[placeholder="Input your email"]').send_keys("admin@admin.ua")

    button = browser.find_element_by_xpath("//button[contains(text(), 'Submit')]")
    button.click()


class TestAbs(unittest.TestCase):
    def test_1(self):
        self.assertEqual(test1(), "Поздравляем! Вы успешно зарегистировались!")

    def test_2(self):
        self.assertEqual(test2(),"Поздравляем! Вы успешно зарегистировались!")


if __name__ == "__main__":
    unittest.main()



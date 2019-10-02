from selenium import webdriver
import time
import unittest


def link_t(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get(link)

    for i in ('first', 'second', 'third'):
        browser.find_element_by_css_selector('div.first_block .' + i).send_keys('knock-knock')
    browser.find_element_by_css_selector("button.btn").click()
    time.sleep(1)
    return browser.find_element_by_tag_name("h1").text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")

    def test_reg2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")


if __name__ == "__main__":
    unittest.main()
from selenium import webdriver

import unittest
import time
class Test1(unittest.TestCase):
    def test1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

    # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
        input3.send_keys("ipetrov@gmail.com")

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
        welcome_text_expected = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual((welcome_text_expected), welcome_text, "Registration error")

    def test2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
        input3.send_keys("ipetrov@gmail.com")

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
        welcome_text_expected = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual((welcome_text_expected), welcome_text, "Registration error")

if __name__ == "__main__":
    unittest.main()
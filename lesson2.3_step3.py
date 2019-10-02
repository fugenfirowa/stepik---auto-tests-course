import os
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button2 = browser.find_element_by_class_name("btn")
    button2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
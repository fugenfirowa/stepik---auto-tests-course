import os
from selenium import webdriver
import time
import math

try:
    link = "https://stepik.org/lesson/236895/step/1"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(10)
    answer = math.log(int(time.time()))
    input1 = browser.find_element_by_tag_name("textarea")
    input1.send_keys(str(answer))
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    result = browser.find_element_by_class_name('smart-hints__hint')
    assert result.text == "Correct!", \
        f"Fail"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
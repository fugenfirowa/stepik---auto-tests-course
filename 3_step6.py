import time
import math

import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_that_checks_links(browser, link):
    link = f"{link}"
    browser.get(link)
    browser.implicitly_wait(20)
    answer = math.log(int(time.time()))
    input1 = browser.find_element_by_tag_name("textarea")
    input1.send_keys(str(answer))
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    browser.implicitly_wait(5)
    result = browser.find_element_by_class_name('smart-hints__hint')
    assert result.text == "Correct!", \
        f"Fail"
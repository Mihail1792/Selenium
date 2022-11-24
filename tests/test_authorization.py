import time
import math

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    # "https://stepik.org/lesson/236897/step/1",
    # "https://stepik.org/lesson/236898/step/1",
    # "https://stepik.org/lesson/236899/step/1",
    # "https://stepik.org/lesson/236903/step/1",
    # "https://stepik.org/lesson/236904/step/1",
    # "https://stepik.org/lesson/236905/step/1",
]


# answer = str(math.log(int(time.time())))


# @pytest.mark.parametrize('answer', str(math.log(int(time.time()))))

# @pytest.mark.parametrize('link', links)
# # вызываем фикстуру в тесте, передав ее как параметр browser
# def test_login_link(browser, link):




from selenium import webdriver
browser = webdriver.Chrome()
link = "https://stepik.org/lesson/236896/step/1"

answer = str(math.log(int(time.time())))
print(f"answer: {answer}, {type(answer)}")
print(link)
# browser.implicitly_wait(10)
browser.get(link)
time.sleep(5)
browser.find_element(By.CSS_SELECTOR,
                     "a.navbar__auth_login").click()
time.sleep(3)

email = browser.find_element(By.NAME, 'login')
email.send_keys("mihail17921792@gmail.com")

password = browser.find_element(By.NAME, 'password')
password.send_keys("stepik1792")

browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
time.sleep(4)


# if browser.find_element(By.CSS_SELECTOR, 'button.again-btn'):
#     browser.find_element(By.CSS_SELECTOR, 'button.again-btn').click()
#     browser.find_element(By.XPATH, '//*[@id="ember124"]/button[1]').click()
# browser.find_element(By.CSS_SELECTOR, 'textarea.ember-text-area').clear()  # .clear() очищает форму
input_answer = browser.find_element(By.CSS_SELECTOR, 'textarea.ember-text-area')
# time.sleep(4)
input_answer.send_keys(answer)
browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
# wait = WebDriverWait(browser, 10)
# button_submit = wait.until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
# button_submit.click()
print("finish test1")
time.sleep(5)
print("finish test1")
browser.quit()

# browser.implicitly_wait(10)
# WebDriverWait EC.element_to_be_clickable

# a = TestMainAuthorization.answer
# print(a)
# print(type(a))
# print(answer)



from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока цена не будет 100
    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    # Жмём кнопку при цене 100
    browser.find_element(By.ID, 'book').click()

    x = browser.find_element(By.ID, 'input_value').text
    input_form = browser.find_element(By.ID, 'answer')
    input_form.send_keys(calc(x))

    browser.find_element(By.ID, 'solve').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()






# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

# Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.

#https://stepik.org/lesson/181384/step/7?unit=156009

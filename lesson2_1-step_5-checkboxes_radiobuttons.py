from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x = browser.find_element(By.ID, 'input_value').text  # Получаем текст "Наш текст" из span
    input_form = browser.find_element(By.ID, 'answer')
    input_form.send_keys(calc(x))
    browser.find_element(By.ID, 'robotCheckbox').click()  # Checkbox
    browser.find_element(By.ID, 'robotsRule').click()  # Radio

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

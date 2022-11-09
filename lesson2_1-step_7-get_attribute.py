from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Сначала ищем сам элемент, потом получаем значение аттрибута
    x = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
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

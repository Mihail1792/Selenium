from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = browser.find_element(By.ID, 'num1').text
    num_2 = browser.find_element(By.ID, 'num2').text
    result = str(int(num_1) + int(num_2))
    # поиск по видимому тексту в выпадающем списке
    select = Select(browser.find_element(By.ID, "dropdown")).select_by_visible_text(result)

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

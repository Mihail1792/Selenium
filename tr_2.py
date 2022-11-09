import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(2)
# скроллим
driver.get("https://dvprogram.state.gov/")
time.sleep(5)

driver.execute_script("window.scrollBy(0, 300);")

time.sleep(15)


# Найдем кнопку, которая отправляет введенное решение
# submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке

submit_button = driver.find_element(By.CLASS_NAME, "btn btn-success")
if submit_button:
    print('tr')
submit_button.click()
time.sleep(10)
print('Ready')

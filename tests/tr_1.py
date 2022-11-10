import time

# webdriver это и есть набор команд для управления браузером
from pip._vendor import requests
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = DesiredCapabilities.CHROME
capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}



# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome(desired_capabilities=capabilities)

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(15)




# Найдем кнопку, которая отправляет введенное решение
# submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
tr = submit_button = driver.find_element(By.NAME, "_ctl0:ContentPlaceHolder1:btnSubmit")
while not tr:
    try:
        # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
        driver.get("https://dvprogram.state.gov/")
        time.sleep(15)
    except:
        pass
print('Ready')

# print(driver.current_url)
#
# def get_status_code(url):
#     for entry in driver.get_log('performance'):
#         for k, v in entry.items():
#             if k == 'message' and 'status' in v:
#                 msg = json.loads(v)['message']['params']
#                 for mk, mv in msg.items():
#                     if mk == 'response':
#                         response_url = mv['url']
#                         response_status = mv['status']
#                         if response_url == url:
#                             return response_status
#
#
# print(get_status_code(driver.current_url))

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
# textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# Напишем текст ответа в найденное поле
# textarea.send_keys("get()")
# time.sleep(5)



# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
# submit_button.click()
# time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
# driver.quit()
def request_partner(**data):
    url = "https://dvprogram.state.gov/"
    req = requests.get(url=url, params=data)
    return req
# print(request_partner())
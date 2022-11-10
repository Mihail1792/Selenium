import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(2)

driver.get('https://tvplus.by/')
time.sleep(2)

# driver.execute_script("window.scrollBy(0, 400);")
# time.sleep(2)

# Найдем кнопку, которая отправляет введенное решение
# submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке

try:
    # кнопка войти
    driver.find_element(By.CSS_SELECTOR, '#__next > div > div.jss19 > header > header > div.jss29 > a').click()
    time.sleep(1)
    # поля ввода
    phone_input = driver.find_element(By.ID, 'formatted-text-mask-input')
    phone_input.clear()
    phone_input.send_keys('257187087')
    time.sleep(1)
    phone_input = driver.find_element(By.ID, 'filled-adornment-password')
    phone_input.clear()
    phone_input.send_keys('zeS32d')
    time.sleep(2)
    # кнопка авторизации
    driver.find_element(By.CSS_SELECTOR,
                        '#loginForm > div > div.jss75 > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.jss77.MuiButton-containedSecondary').click()
    time.sleep(8)
    # выбор вкладки амедиатеки
    driver.find_element(By.CSS_SELECTOR,
                        '#__next > div > div.jss19 > header > header > div.jss28 > div > div > div > a:nth-child(2)').click()
    time.sleep(10)
    print('выбор вкладки амедиатеки')
    # Дом дракона выбор
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div/div[1]/div[1]/div[1]/div[1]/a/div/button').click()
    time.sleep(6)
    print('Дом дракона выбор')
    driver.execute_script("window.scrollBy(0, 550);")
    time.sleep(3)
    # Кнопка плей на плеере
    player = driver.find_element(By.CSS_SELECTOR,
                                 '#__next > div > div.jss19 > div > div > div.jss540 > div > div.jss593 > div > div > div.swiper-slide.jss594.swiper-slide-active > div.jss595.jss607')
    driver.execute_script("arguments[0].click();", player)
    driver.execute_script("arguments[0].click();", player)
    time.sleep(20)

finally:
    driver.quit()







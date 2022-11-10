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
driver.get("http://amediateka.tvplus.by/")
time.sleep(2)

# Найдем кнопку, которая отправляет введенное решение
# submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке

submit_button = driver.find_element(By.XPATH, '//*[@id="checkbox"]')
driver.execute_script("arguments[0].click();", submit_button)
time.sleep(3)
driver.find_element(By.ID, 'hider').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#__next > div > div.jss19 > header > header > div.jss29 > a').click()
time.sleep(1)

phone_input = driver.find_element(By.ID, 'formatted-text-mask-input')
phone_input.clear()
phone_input.send_keys('257187087')
time.sleep(1)
phone_input = driver.find_element(By.ID, 'filled-adornment-password')
phone_input.clear()
phone_input.send_keys('zeS32d')
time.sleep(2)
# кнопка авторизации
driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div.jss75 > button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.jss77.MuiButton-containedSecondary').click()
time.sleep(6)
# выбор вкладки амедиатеки
driver.find_element(By.CSS_SELECTOR, '#__next > div > div.jss19 > header > header > div.jss28 > div > div > div > a:nth-child(2)').click()
# Дом дракона выбор
driver.find_element(By.CSS_SELECTOR, '#__next > div > div.jss19 > div > div.jss1943 > div.swiper-container.swiper-container-initialized.swiper-container-horizontal > div.swiper-wrapper > div.swiper-slide.swiper-slide-active > a > div').click()
time.sleep(3)
# Кнопка плей на плеере
driver.find_element(By.CSS_SELECTOR, '#__next > div > div.jss19 > div > div > div.jss1195 > div > div.jss1248 > div > div > div.swiper-slide.jss1249.swiper-slide-active > div.jss1250.jss1262 > svg > path').click()


# driver.quit()


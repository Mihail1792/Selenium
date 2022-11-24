# Чтобы указать язык браузера с помощью WebDriver, используйте класс Options и метод add_experimental_option,
# как указано в примере ниже:


from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

# Для Firefox объявление нужного языка будет выглядеть немного иначе:

fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)

# В конструктор webdriver.Chrome или webdriver.Firefox вы можете добавлять разные аргументы, расширяя возможности
# тестирования ваших веб-приложений: можно указывать прокси-сервер для контроля сетевого трафика или запускать разные
# версии браузера, указывая локальный путь к файлу браузера. Предполагаем, что эти возможности вам понадобятся позже и
# вы сами сможете найти настройки для этих задач.

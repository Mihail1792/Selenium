# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


# catalog_text = 'kek'  # считываем текст и записываем его в переменную
# assert catalog_text == "Каталог", f"Wrong language, got {catalog_text} instead of 'Каталог'"

def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == 8, f"Получили: {actual_result} Ожидали: {expected_result}"

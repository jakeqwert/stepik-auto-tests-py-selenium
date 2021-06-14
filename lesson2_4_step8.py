# -*- coding: utf-8 -*-

# pip install selenium
# качаем драйвер для браузера, такой же версии, что и браузер на компьютере
# Selenium требует драйвера для взаимодействия с выбранным браузером. Например, для Firefox требуется geckodriver,
# Убедитесь, что он находится в вашем PATH, например, поместите его в /usr/bin или /usr/local/bin
# Несоблюдение этого шага приведет к ошибке selenium.common.exceptions.WebDriverException: Сообщение:
# исполняемый файл 'geckodriver' должен находиться в переменной PATH.
# Другие поддерживаемые браузеры будут иметь свои собственные драйверы.
# Хром :	https://sites.google.com/a/chromium.org/chromedriver/downloads
# Firefox :	https://github.com/mozilla/geckodriver/releases

# скачать тут
# Chromedriver: https://chromedriver.storage.googleapis.com/index.html
# Geckodriver: https://github.com/mozilla/geckodriver/releases


# Home:	http://www.seleniumhq.org
# Docs:	selenium package API
# Dev:	https://github.com/SeleniumHQ/Selenium
# PyPI:	https://pypi.org/project/selenium/


# для прокси с авторизацией нужна еще библиотека pip install selenium-wire
import math

from selenium import webdriver
# from seleniumwire import webdriver  # появяться доп возможности для работы с параметрами/опциями
# браузера

import os
import time

import random
from fake_useragent import UserAgent  # pip install fake-useragent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from proxy_auth_data import login, password  # файл py с переменными

# driver = webdriver.Chrome(executable_path="./chromedriver/chromedriver")  # путь относительно
# папки проекта или абсолютный путь "./chromedriver/chromedriver"
# для win "C:\\user\\selenium\\chromedriver\\chromedriver.exe"
# для win "сырые строки" r"C:\user\selenium\chromedriver\chromedriver.exe"

# os.chmod('./chromedriver', 0o755)  # права на файл дожны быть 755

# url = "https://instagram.com/"

# user_agents_list = [
#     "hello_world",
#     "best_of_the_best",
#     "python_today"
# ]

# options опции браузера https://peter.sh/experiments/chromium-command-line-switches/
# options = webdriver.ChromeOptions()
# options.add_argument()

# change useragent
# useragent = UserAgent()

# добавили user-agent
# options.add_argument("user-agent=HelloWorld:)")
# options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
# options.add_argument(f"user-agent={useragent.random}")

# set proxy, как новый аргумент опции браузера хром
# анонимный прокси
# options.add_argument("--proxy-server=138.128.91.65:8000")

# прокси с авторизацией
# для прокси с авторизацией нужна еще библиотека pip install selenium-wire
# proxy_options = {
#     "proxy": {
#         # протокол : параметры
#         "https": f"http://{login}:{password}@138.128.91.65:8000"
#     }
# }

# driver = webdriver.Chrome(
#     executable_path="./chromedriver/chromedriver",
#     options=options
# )

# driver
browser = webdriver.Chrome(executable_path="./chromedriver")
# seleniumwire_options=proxy_options
# )

# В официальном магазине расширений есть расширение Buster Captcha Solver, она единственная из многих реально хорошо решает
# reCAPTCHA(+ ко всему бесплатная). И гугл ёё не удаляет...был удивлен, так к сведению, может быть будет полезно.

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"

    # Открыть страницу
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить
    # не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажать на кнопку
    button.click()

    # x
    span_x = browser.find_element_by_id("input_value")
    text_x = span_x.text
    x = int(text_x)

    # Посчитать математическую функцию от x (код для этого приведён ниже).
    y = calc(x)

    input_answer = browser.find_element_by_id("answer")
    # Ввести ответ в текстовое поле.
    input_answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    button.click()



except Exception as ex:
    print(ex)
finally:  # всегда выполняется, закроем драйвер
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(100)
    # закрываем браузер после всех манипуляций
    browser.close()
    browser.quit()
# не забываем оставить пустую строку в конце файла
# Системы UNIX/Linux ожидают пустую строку в конце файла, если в вашем скрипте ее не будет, то последняя строчка, содержащая код, может не выполниться.

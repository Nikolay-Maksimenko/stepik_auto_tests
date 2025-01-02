from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    first_name.send_keys('Test')
    last_name = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    last_name.send_keys('Test')
    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    email.send_keys('Test')
    file = browser.find_element(By.CSS_SELECTOR, "input[name='file']")
    file.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
# print(os.path.abspath(__file__))
# print()
# print(os.path.abspath(os.path.dirname(__file__)))
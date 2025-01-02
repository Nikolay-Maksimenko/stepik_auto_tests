import math

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num_1 = browser.find_element(By.ID, "num1").text
    num_2 = browser.find_element(By.ID, "num2").text
    sum_el = int(num_1) + int(num_2)
    print(sum_el)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(sum_el))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
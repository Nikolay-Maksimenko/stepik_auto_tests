from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = int(browser.find_element(By.ID, "input_value").text)
    result = math.log(abs(12 * math.sin(x)))
    input_result = browser.find_element(By.ID, "answer")
    input_result.send_keys(result)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
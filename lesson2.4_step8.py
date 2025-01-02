from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

# from stepic.lesson6_step11 import button

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button = browser.find_element(By.ID, "book")
button.click()

x = int(browser.find_element(By.ID, "input_value").text)
result = math.log(abs(12 * math.sin(x)))
input_result = browser.find_element(By.ID, "answer")
input_result.send_keys(result)
button = browser.find_element(By.ID, "solve")
button.click()
time.sleep(10)

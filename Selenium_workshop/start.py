from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('https://www.sofascore.com/')
print(driver.title)
time.sleep(3)
driver.maximize_window()
driver.find_element(By.CLASS_NAME,'fc-button-label').click()

search_bar = driver.find_element(By.CSS_SELECTOR,'input.sc-30244387-0.hiFyBG')
search_bar.send_keys("puchar polski")
search_bar.send_keys(Keys.RETURN)

time.sleep(15)

driver.close()
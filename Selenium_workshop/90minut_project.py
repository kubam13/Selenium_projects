from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('http://www.90minut.pl/')
print(driver.title)
time.sleep(3)
driver.maximize_window()
cookies_ok = driver.find_element(By.CLASS_NAME, 'css-2evfjs')
cookies_ok.click()
transfers = driver.find_element(By.XPATH, '/html/body/table[2]/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/div[8]/a')
transfers.click()
time.sleep(5)
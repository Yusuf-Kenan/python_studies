from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
url =  "https://github.com/"
driver.get(url)
searchButton = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/button").click()
time.sleep(1)
searchInput = driver.find_element(By.XPATH, '//*[@id="query-builder-test"]')
searchInput.send_keys("selenium")
time.sleep(1)
searchInput.send_keys(Keys.ENTER)
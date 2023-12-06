from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from insta_user_info import username, password

driver = webdriver.Firefox()
url =  "https://www.instagram.com/"
driver.get(url)
time.sleep(2)
userName = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
passWord = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
time.sleep(2)
userName.send_keys(username)
passWord.send_keys(password)
time.sleep(2)
passWord.send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a").click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="mount_0_0_Q1"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a').click()
time.sleep(2)
driver.get(url+username)
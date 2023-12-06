import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from youtube_user_info import users
from tube_play_list import play_list


for user in users:
    browser = uc.Chrome()
    browser.get("https://www.youtube.com/")
    time.sleep(2)

    browser.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/ div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a").click()
    time.sleep(2)
    user_name = browser.find_element(By.XPATH, '//*[@id="identifierId"]')
    user_name.send_keys(user["user_name"])
    user_name.send_keys(Keys.ENTER)

    time.sleep(3)
    password = browser.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    password.send_keys(user["password"])
    password.send_keys(Keys.ENTER)

    for song in play_list:
        time.sleep(3)
        browser.get(song["link"])
        time.sleep(song["time"]+3)
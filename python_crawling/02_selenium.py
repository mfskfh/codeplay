import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


broweer = webdriver.Chrome()

broweer.get("https://www.op.gg/champions")

elem = broweer.find_element(By.ID, "search")
elem.send_keys("실력이너무낮다")
time.sleep(1)
elem.send_keys(Keys.ENTER)

time.sleep(1)
broweer.get("https://naver.com")

elem = broweer.find_element(By.ID, "query")
elem.send_keys("아리")
time.sleep(1)
elem.send_keys(Keys.ENTER)

time.sleep(1)
broweer.get("https://dinorunner.com/ko/")

elem = broweer.find_element(By.CLASS_NAME, "game__start")
time.sleep(1)
elem.click()
elem = broweer.find_element(By.CLASS_NAME, "runner-canvas")
time.sleep(1)
elem.send_keys(Keys.SPACE)



while True:
    if "q" == input("quit?"):
        break
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import lxml
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
user = input("소환사이름 입력 : ")
url= f"https://www.op.gg/summoners/kr/{user}"
user = 0

browser.get(url)

soup = BeautifulSoup(browser.page_source, "lxml")
fellow = soup.find_all("td", attrs = {"class" : "name"})
print("최근 같은팀")
for i in fellow:
    print(i.get_text())
win_lose = soup.find("div", attrs={"class" : "stats"})
print(win_lose.get_text())
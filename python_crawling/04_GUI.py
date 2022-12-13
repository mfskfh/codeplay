import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import lxml
from bs4 import BeautifulSoup
import tkinter as tk
import tkinter.font as ft

lol = tk.Tk()

lol.title("계산기")
lol.geometry("800x600")

dp = tk.Entry(lol, width = 100)
dp.pack()

fontconfig = ft.Font(family = "Malgun Gothic", size = 15 , weight = "bold")

browser = webdriver.Chrome()
user = 0

def sel_search(name):
    url = f"https://www.op.gg/summoners/kr/{name}"
    browser.get(url)
    time.sleep(1)
    soup = BeautifulSoup(browser.page_source, "lxml")
    fellow = soup.find_all("td", attrs = {"class" : "name"})
    for i in fellow:
        fellow.append(i.get_text())
    win_lose = soup.find("div", attrs={"class" : "stats"})
    print("최근 같은팀")
    label_show(win_lose)

def label_show(label):
    show = tk.Label(lol, text = label, fg="white", bg="black", width = 20)
    show.configure(font = fontconfig)
    show.pack(side = "top")

def user_find(event):
    result = tk.Entry.get(dp)
    label_show(result)
    user = result
    dp.delete(0, tk.END)
    sel_search(result)

lol.bind("<Return>", user_find)

lol.mainloop()
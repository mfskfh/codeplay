import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()

# browser.get("https://www.op.gg/")

# elem = browser.find_element(By.ID, "searchHome")
user = "실력이너무낮다"
# elem.send_keys(user)
# time.sleep(1)
# elem.send_keys(Keys.ENTER)

# time.sleep(1)

user_list = []
browser.get(f"https://www.op.gg/summoners/kr/{user}")
time.sleep(1)

elem = browser.find_element(By.CLASS_NAME, "tier")
time.sleep(1)
user_list.append(elem.text)

elem = browser.find_element(By.CLASS_NAME, "lp")
time.sleep(1)
user_list.append(elem.text)

elem = browser.find_elements(By.CLASS_NAME, "k-d-a")
time.sleep(1)
user_list.append(elem[1].text)

print(user_list)

# while True:
#     if "q" == input("quit?"):
#         break
import requests
from bs4 import BeautifulSoup

site = requests.get('https://www.op.gg/summoners/kr/KJGKRF%EC%A1%B0%EC%9A%B0%EC%A7%84')
sourse = BeautifulSoup(site.text, 'html.parser')
issue = sourse.select('.info .rank')

# for title in issue:
#     print(title.get_text())
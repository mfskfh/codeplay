import requests
import lxml
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/weekday" #웹사이트 주소

headers = {"acceot-language" : "ko_KR", "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

resource = requests.get(url, headers = headers)
resource.raise_for_status()

soup = BeautifulSoup(resource.text, "lxml")

monday1 = soup.find("a", attrs = {"class" : "title"})

monday2 = monday1

print(monday1.get_text(), monday2.get_text())

# monday = allday.find("div", attrs = {"class" : "thumb"})
# print(monday)

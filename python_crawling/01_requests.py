import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.op.gg/champions" #웹사이트 주소

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

resource = requests.get(url, headers = headers)
resource.raise_for_status()

with open("opgg.html", "w", encoding = "utf-8") as file:
    file.write(resource.text)


soup = BeautifulSoup(resource.text, "lxml") #긁어온 사이트를 lxml 로 읽어들여 뷰티풀숩에서 soup에 객채로 담아둠
print(soup.title) #title html 태그를 찾아 출력 (가장먼저 걸리는 데이터)
print(soup.title.get_text()) #태그빼고 내용물만 보여줌
print(soup.a)
print(soup.a.attrs) #a 태그가 가지는 속성들이 있으면 나열해 보여줌
print(soup.a["href"]) #a 태그 안에 포합된 href라는 속성의 값을 보여줌

print(soup.find("a", attrs = "/champions/varus/mid?region=ru&tier=iron")) #a 태그중 ㄷㄷ
print(soup.find(attrs = "/champions/varus/mid?region=ru&tier=iron"))
print(soup.find("a", attrs = "/champions/varus/mid?region=ru&tier=iron").get_text())
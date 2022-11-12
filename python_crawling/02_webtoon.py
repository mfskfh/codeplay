import requests
import lxml
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/weekday" #웹사이트 주소

headers = {"acceot-language" : "ko_KR", "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

resource = requests.get(url, headers = headers)
resource.raise_for_status()

soup = BeautifulSoup(resource.text, "lxml")

# sat_all = soup.find("div", attrs={"class" : "col col_selected"})
# # print(sat_all)

# sat_all_title = sat_all.find_all("a", attrs={"class" : "title"})
# # print(sat_all_title[0].get_text())

count = 1

# for top10 in sat_all_title:
#     print(f"토요웹툰 {count}위 : {top10.get_text()}")
#     count += 1
#     if count > 10:
#         break

week_all = soup.find_all("div", attrs={"class" : "col"})
wed_all = week_all[2]
wed_all_title = wed_all.find_all("a", attrs={"class" : "title"})

for top10 in wed_all_title:
    print(f"수요웹툰 {count}위 : {top10.get_text()}")
    count += 1
    if count > 10:
        break

count = 1

popularity_webtoon = soup.find("ol", attrs={"class" : "asideBoxRank"})
popularity_webtoon_title = popularity_webtoon.find_all("a")

for top10 in popularity_webtoon_title:
    print(f"인기급상승웹툰 {count}위 : {top10.get_text()}")
    count += 1
    if count > 10:
        break

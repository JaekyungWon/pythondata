import urllib.request
from matplotlib.pyplot import title
import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/movies/'
# res = urllib.request.urlopen(url)
res = requests.get(url).text
soup = BeautifulSoup(res,'lxml')
# print(soup.prettify())

# 영화 제목 가져오기
result = soup.select('strong.title')
movieName = []
for item in result:
    movieName.append(item.text)
# print(movieName)

# 영화 포스터 이미지 가져오기
result2 = soup.select('span.thumb-image>img')
moviePoster = []
for item in result2:
    moviePoster.append(item['src'])
# print(moviePoster)
print(list(zip(movieName, moviePoster)))


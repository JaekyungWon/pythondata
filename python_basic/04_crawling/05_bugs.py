import requests
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'
res = requests.get(url).text
soup = BeautifulSoup(res, 'lxml')

# 노래 제목 가져오기
result = soup.select('p.title > a')
song = []
for i in result:
    song.append(i.text)
# print(song)

# 가수 이름 가져오기
result2 = soup.select('p.artist > a:nth-of-type(1)')
artist = []
for i in result2:
    artist.append(i.text)
# print(len(artist)) -> p.artist a 만 하면 105개가 나오니까 nth=of-type(1)해서 p.artist 값 중 첫번째 값만 가져오기

print(list(zip(song, artist)))

import requests
from bs4 import BeautifulSoup

url='https://www.starbucks.co.kr/store/store_map.do'
res = requests.get(url).text
soup = BeautifulSoup(res, 'lxml')

result = soup.select_one('li.quickResultLstCon')

print(result)
# 결과 값은 none : 기본 틀만 놔두고 데이터는 나중에 받아오는 식이기 때문. 이럴 때 가져오려면 selenium 쓰면 된다.
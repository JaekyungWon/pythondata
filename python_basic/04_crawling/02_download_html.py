# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%97%AC%EB%A6%84%EB%B0%94%EB%8B%A4

import urllib.request   #url가지고 올 때
import urllib.parse     #url query=%EC% <-이거 한글인데 이렇게 나온거라서 바꿔주는 것

url = 'https://search.naver.com/search.naver'
values={    #url 뒤에 남은 주소들 &을 기준으로 나눠서 딕셔너리로 만들기
    'where':'nexearch',
    'sm':'top_hty',
    'fbm':'0',
    'ie':'utf8',
    'query': '여름바다'
}
param = urllib.parse.urlencode(values)
url = url + '?' + param
print(url)

data = urllib.request.urlopen(url).read().decode('utf-8')
print(data)
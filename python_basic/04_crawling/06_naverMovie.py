# import urllib.request
import requests
from bs4 import BeautifulSoup
import re

url = 'https://movie.naver.com/movie/point/af/list.naver?page={}'
reviewlist = []
for i in range(1,11):
    print(url.format(i))
    res = requests.get(url.format(i)).text
    soup = BeautifulSoup(res, 'lxml')
    table = soup.find('table', class_='list_netizen')
    for i,r in enumerate(table.select('tbody tr')):
        for j,c in enumerate(r.find_all('td')):
            # 첫번째 칸 - 글번호
            if j == 0:
                recode = int(c.text.strip())
                # print('글번호 : ', recode)
            # 두번째 칸 - 제목, 평점, 리뷰
            elif j ==1:
                recode1 = c.select_one('a').text.strip()
                # print('영화 제목 : ', recode1)
                recode2 = c.select_one('em').text
                # print('영화 평점 : ', recode2)
                recode3 = c.text.strip()
                recode3 = recode3.replace(recode1, '').strip()      # 영화 제목 없애기
                recode3 = recode3.replace('신고', '').strip()       # 신고 글자 없애기
                recode3 = re.sub('별점 - 총 10점 중[0-9]{1,2}','',recode3).strip()                          # re.sub(패턴, 바꿀 문자열, recode3)
                # print('리뷰 : ', recode3)
                try:
                    movie_dic={
                        '제목' : recode1,
                        '평점' : recode2,
                        '리뷰' : recode3
                    }
                    reviewlist.append(movie_dic)
                except:     #리뷰 내용 없을 때 예외처리
                    pass

print(reviewlist)

# soup.select, selectone : css 이용 하는 것
# soup.find

# # 영화 제목
# title = soup.select('td.title > a.movie')
# titles = []
# for i in title:
#     titles.append(i.text)
# # print(titles)

# # 평점
# star = soup.select('div.list_netizen_score > em')
# stars = []
# for i in star:
#     stars.append(i.string)
# # print(stars)

# # 후기
# article = soup.select('td.title')
# articles = []
# for i in article:
#     articles.append(i.text)
# print(articles)

# print(list(zip(titles,stars,articles)))
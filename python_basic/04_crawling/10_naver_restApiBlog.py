import os, sys, urllib.request, json

client_id = "6P2SU_vKNi35LoyPY2D8"
client_secret = "9IPL_mpBCM"

keyword = input('검색할 단어 >>> ')
encText = urllib.parse.quote(keyword)
url = "https://openapi.naver.com/v1/search/blog?display=10&query=" + encText # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

# 블로그 글 검색해서 가져오기
if(rescode==200):
    response_body = response.read()
    # print(type(response_body.decode('utf-8')))      #type : str
    result = json.loads(response_body)
    # print(result)     #type : dictionary
    for item in result['items']:
        print(item['bloggerlink'])
        res = urllib.request.urlopen(item['bloggerlink']).read()
        print(res.decode('utf-8'))
else:
    print("Error Code:" + rescode)


import os, sys, urllib.request, json

client_id = "6P2SU_vKNi35LoyPY2D8"
client_secret = "9IPL_mpBCM"

keyword = input('검색할 단어 >>> ')
encText = urllib.parse.quote(keyword)
url = "https://openapi.naver.com/v1/search/news.json?display=10&query=" + encText # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    try:
        response_body = response.read()
        result = json.loads(response_body)
        # print(result)
        for item in result['items']:
            print(item['link'])
            res = urllib.request.urlopen(item['link']).read()
            # print(res.decode('utf-8'))
    except:
        pass

else:
    print("Error Code:" + rescode)

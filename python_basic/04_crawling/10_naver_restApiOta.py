import os, sys, urllib.request, json

client_id = "6P2SU_vKNi35LoyPY2D8"
client_secret = "9IPL_mpBCM"

keyword = input('검색할 단어 >>> ')
encText = urllib.parse.quote(keyword)
url = "https://openapi.naver.com/v1/search/errata.json?query=" + encText # json 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

print(response.read().decode('utf-8'))
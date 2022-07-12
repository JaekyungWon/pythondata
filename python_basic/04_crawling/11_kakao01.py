'''
curl -v -X GET "https://dapi.kakao.com/v2/local/search/address.json" \
  -H "Authorization: KakaoAK ${REST_API_KEY}" \
  --data-urlencode "query=전북 삼성동 100" 
'''

import requests
REST_API_KEY = '706b841e9c08dc6e0427fde5fd745062'
headers = {'Authorization': f'KakaoAK {REST_API_KEY}'}
addr = input('주소를 입력하세요 >>> ')
url = f"https://dapi.kakao.com/v2/local/search/address.json?query={addr}"
r = requests.get(url,headers=headers)       #type : dictionary
data = r.json()
print('경도 : ', data['documents'][0]['x'])
print('위도 : ', data['documents'][0]['y'])

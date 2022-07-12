from selenium import webdriver
import time, os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')
driver.get('https://www.naver.com')

# 네이버 검색창에 input box id로 찾기
query = driver.find_element(By.ID, 'query')
# 입력창에 뭐가 있다면 없애 주는 것
query.clear()
# send_keys
query.send_keys('아이유')
time.sleep(3)
# Keys import 할 것
query.send_keys(Keys.ENTER)
time.sleep(3)
blogcontent = driver.find_element(By.CLASS_NAME, 'total_wrap')
blogcontent.click()
time.sleep(3)
print(driver.page_source)
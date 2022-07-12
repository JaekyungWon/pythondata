from this import d
from selenium import webdriver
import os, time

path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')

driver.implicitly_wait(15)
driver.get('https://www.google.co.kr')
time.sleep(3)       #대기하는 게 없으면 휙휙 지나가서 안보임
driver.get('https://www.youtube.com')
time.sleep(3)
driver.get('https://www.naver.com')
time.sleep(3)

# 뒤로가기 버튼이랑 같은 기능
driver.back()
time.sleep(3)
driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)
driver.forward()
time.sleep(3)

driver.quit()
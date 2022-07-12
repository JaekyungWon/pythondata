from selenium import webdriver

import os, time

path = os.path.dirname(__file__)        #현재 실행중인 파일의 경로가 들어 있고 directory 이름만 추출 하는 메소드

driver = webdriver.Chrome(path+'/driver/chromedriver')
# implicitly_wait는 안줘도 문제가 없는 경우도 있음. 인터넷 상황에 따라 다르다
driver.implicitly_wait(15)

# 인터넷 브라우저 창 전체화면으로 보여주는 것 (default는 이전 설정 그대로 감)
driver.fullscreen_window()
time.sleep(3)
# 브라우저 창 최소화
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.set_window_rect(100,100, 500,500)
time.sleep(3)
print(driver.get_window_rect())
time.sleep(3)
driver.set_window_position(0,0)
time.sleep(3)
driver.quit()

# 처음 받은 소스에 데이터가 없는 경우 selenium 이용할 것
# selenium 만들어진 목적 : 만들고 나서 기능 테스트 하기 위한 용도로 만들어진 라이브러리였다
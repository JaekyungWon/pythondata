from selenium import webdriver
import os, time

path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')

# 창이 제대로 뜰 때 까지 15초까지 대기하겠다는 뜻 (기본 단위는 초)
driver.implicitly_wait(15)
driver.get('https://google.co.kr')
time.sleep(5)       #5초 대기하는 것
driver.quit()       #프로그램 종료
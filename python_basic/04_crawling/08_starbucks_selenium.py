import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time, os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')

driver.implicitly_wait(15)
driver.get('https://www.starbucks.co.kr/store/store_map.do')
time.sleep(8)

'''
soup = BeautifulSoup(driver.page_source, 'lxml')
result = soup.select('ul.quickSearchResultBox > li')
for i in result:
    print(i.text)
'''
localSearch = driver.find_element(By.CLASS_NAME, 'loca_search')
localSearch.click()
time.sleep(5)
clickCido = driver.find_element(By.CLASS_NAME, 'sido_arae_box')
lis = clickCido.find_elements(By.TAG_NAME, 'li')
lis[5].click()
time.sleep(5)
gugun = driver.find_element(By.CLASS_NAME, 'gugun_arae_box')
gulis = gugun.find_elements(By.TAG_NAME,'li')
gulis[3].click()
time.sleep(20)
result = driver.find_elements(By.CSS_SELECTOR, 'ul.quickSearchResultBoxSidoGugun > li')
for i in result:
    print('매장이름 : ', i.find_element(By.TAG_NAME,'strong').text)
    print('매장주소 : ', i.find_element(By.TAG_NAME,'p').text)
    print()
from bs4 import BeautifulSoup
from selenium import webdriver
import time, os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')

driver.get('https://nid.naver.com/nidlogin.login?')
driver.implicitly_wait(10)

# id = driver.find_element(By.ID, 'id')
# id.clear()
# id.send_keys('jaekyung43')

# pw = driver.find_element(By.ID, 'pw')
# pw.clear()
# pw.send_keys('Eofkfl:9782')       #비밀번호라서 네이버는 send_keys로 하면 로그인 안된다
# time.sleep(3)

id='jaekyung43'
pw='Eofkfl:9782'

# javascript 실행하는 것
driver.execute_script("document.getElementById('id').value=\'"+id+"\'")
driver.execute_script("document.getElementById('pw').value=\'"+pw+"\'")
time.sleep(5)

btn = driver.find_element(By.CLASS_NAME, 'btn_login')
btn.click()

btn = driver.find_element(By.CLASS_NAME, 'btn_cancel')
btn.click()
time.sleep(5)

driver.get('https://order.pay.naver.com/home')
npoint = driver.find_element(By.CSS_SELECTOR,'dl > dd > a > strong')
print(npoint)
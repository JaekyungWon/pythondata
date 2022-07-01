import sqlite3

conn = sqlite3.connect('python_basic/03_db/example.db')
cur = conn.cursor()

keyword = input('검색어를 입력하세요 >>>')
sql = 'select * from stocks where symbol = ?'

cur.execute(sql,(keyword,))		#튜플일 경우 변수 하나면 ,찍어줘야 된다
data = cur.fetchall()           #쿼리문에 해당 되는 내용들을 data에 저장

for i in data:
    print(i)

# conn.commit()
conn.close()
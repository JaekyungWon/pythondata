import cx_Oracle

# print(cx_Oracle.version)      #version : 8.3.0

# id/pw@호스트이름:포트/sid
conn = cx_Oracle.connect('python/123@localhost:1521/xe')
cur = conn.cursor()

# insert해보기
idx = input('index값을 입력하세요>>>')
name = input('이름을 입력하세요>>>')
content = input('내용을 입력하세요>>>')

# oracle은 값 받는거 ?,? 아니고 :1, :2 이렇게 쓰면 된다
sql = 'insert into board values(:1, :2, :3)'
cur.execute(sql,(idx,name,content))

conn.commit()

# select해보기
sql = 'select * from board'
cur.execute(sql)
data = cur.fetchall()
for i in data:
  print(i)

conn.close()

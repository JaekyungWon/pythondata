import sqlite3

conn = sqlite3.connect('python_basic/03_db/example.db')
cur = conn.cursor()

data = [('2006-03-28', 'BUY', 'IBM', 300.0, 45.00),
        ('2006-04-03', 'BUY', 'MSFT', 1000.0, 23.20),
        ('2006-05-05', 'SELL', 'IBM', 500.0, 74.53)]
sql = 'insert into stocks values(?,?,?,?,?)'

# 여러 개 실행할 때는 executemany 사용
cur.executemany(sql, data)
conn.commit()
conn.close()
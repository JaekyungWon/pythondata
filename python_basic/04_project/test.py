import sqlite3, sys
class test:
    def tests(self):
        display = input('''
    =======================================================
    1. create
    2. insert
    3. select
    4. 종료
    =======================================================
    >>>''')
        if display =='1':
            self.create_rentTable()            
        elif display == '2':
            self.insert_rentTable()
        elif display == '3':
            self.select_rentTable()
        elif display =='4':
            sys.exit()
        else:
            print('다시입력')

    def __init__(self):
        while True:
            self.tests()

    def create_rentTable(self):
        con = sqlite3.connect('python_basic/04_project/test.db')
        cur = con.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS TEST(
            rid integer,
            rday date
        )
        ''')
        con.commit()
        con.close()
    def insert_rentTable(self):
        con = sqlite3.connect('python_basic/04_project/test.db')
        cur = con.cursor() 
        
        sql = 'INSERT INTO TEST VALUES(?)'
        rid = input('대출아이디를 입력하세요 >>>')
        rday = cur.execute("SELECT date('now','start of month','+14 day')")
        cur.execute(sql,(rid,rday))

        con.commit()
        con.close()

    def select_rentTable(self):
        con = sqlite3.connect('python_basic/04_project/test2.db')
        cur = con.cursor() 
        
        sql = 'SELECT RID, RDAY FROM TEST2'
        cur.execute(sql)
        data = cur.fetchall()
        for i in data:
            print(i)
test()


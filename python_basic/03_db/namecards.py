# 명함관리 프로그램 : db에 데이터가 저장되어야 함
# -명함 등록(일련번호-pk, 이름, 전화번호, fax, 회사명)
# -명함 수정
# -명함 삭제
# -명함 리스트
# -종료

import sqlite3, sys

class ManageCards:

    # 명함 프로그램 실행
    def nameCards(self):
        menu = input('''
=======================================================
1.명함 등록 2.수정 3.삭제 4.명함 리스트 보기 5. 종료
=======================================================
>>>''')
        if menu=='1':
            self.create_card()
            self.insert_card()
        elif menu=='2':
            self.update_card()
        elif menu=='3':
            self.delete_card()
        elif menu=='4':
            self.select_card()
        elif menu=='5':
            print('종료~')
            sys.exit()
        else:
            print('1~5까지 숫자를 선택해주세요')
    
    # 생성자
    def __init__(self):
        while True:
            self.nameCards()

    # cards table 만드는 함수
    def create_card(self):
        conn = sqlite3.connect('python_basic/03_db/namecards.db')
        cur = conn.cursor()
        cur.execute('''
    create table if not exists cards(
        idx integer,
        name text,
        tel text,
        fax text,
        company text
    )
    ''')
        conn.commit()
        conn.close()

    # insert(명함 등록) 함수
    def insert_card(self):
        conn = sqlite3.connect('python_basic/03_db/namecards.db')
        cur = conn.cursor()

        # idx = cur.execute('select ifnull(max(idx),0)+1 as idx from cards')
        
        while True:
            idx = input('일련번호를 입력하세요 >>>')
            if idx.isdigit():
                break
        name = input('이름을 입력하세요 >>>')
        tel = input('전화번호를 입력하세요 >>>')
        fax = input('팩스번호를 입력하세요 >>>')
        company = input('회사이름을 입력하세요 >>>')

        sql='insert into cards values(?,?,?,?,?)'
        cur.execute(sql,(idx,name,tel,fax,company))

        conn.commit()
        print('등록 완료!')
        conn.close()

    # select (명함 리스트) 함수
    def select_card(self):
        conn = sqlite3.connect('python_basic/03_db/namecards.db')
        cur = conn.cursor()

        choice = input('1. 일련번호 순 2. 이름 순>>>')
        if choice == '1':
            sql = 'select idx,name,tel,fax,company from cards order by idx asc'
            cur.execute(sql)
            data = cur.fetchall()
            for i in data:
                print(i)
        elif choice =='2':
            sql = 'select idx,name,tel,fax,company from cards order by name asc'
            cur.execute(sql)
            data = cur.fetchall()
            for i in data:
                print(i)
        else:
            print('1 또는 2를 입력하세요')

        conn.close()

    # update (명함 수정) 함수
    def update_card(self):
        conn = sqlite3.connect('python_basic/03_db/namecards.db')
        cur = conn.cursor()

        sql = 'select idx,name,tel,fax,company from cards order by idx asc'
        cur.execute(sql)
        data = cur.fetchall()
        for i in data:
            print(i)

        idx = input('수정할 명함의 idx를 입력하세요 >>>')
        
        col = input('수정할 컬럼을 입력하세요(name, tel, fax, company) >>>')
        updatedVal = input('수정할 내용을 입력하세요 >>>')

        sql = f'update cards set {col}=? where idx = ?'
        cur.execute(sql,(updatedVal, idx))
        
        conn.commit()
        print('수정 완료~')
        conn.close()

    # delete(명함 삭제) 함수
    def delete_card(self):
        conn = sqlite3.connect('python_basic/03_db/namecards.db')
        cur = conn.cursor()

        sql = 'select idx,name,tel,fax,company from cards order by idx asc'
        cur.execute(sql)
        data = cur.fetchall()
        for i in data:
            print(i)
            
        name = input('삭제할 명함 이름을 입력하세요 >>>')
        sql = 'delete from cards where name like "%" || ? || "%"'
        cur.execute(sql,(name,))

        conn.commit()
        print(f'{name} 데이터가 삭제되었습니다.')
        conn.close()

ManageCards()
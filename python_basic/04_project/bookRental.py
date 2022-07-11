from distutils.log import error
import sqlite3, sys
from turtle import update

# class 활용
class bookRental:
    def display(self):
        RentalServiceDisplay = input('''
=======================================================
1. 회원 등록, 수정, 삭제, 리스트 보기
2. 도서 등록, 수정, 삭제, 리스트 보기
3. 대출
4. 반납, 반납일 조회
5. 종료 
=======================================================
>>>''')
        # 회원 등록, 수정, 삭제, 리스트 보기
        if RentalServiceDisplay == '1':
            self.memberService()
        # 도서 등록, 수정, 삭제, 리스트 보기
        elif RentalServiceDisplay =='2':
            self.bookService()
        # 대출
        elif RentalServiceDisplay =='3':
            self.insertRent()
        elif RentalServiceDisplay =='4':
            pass
        elif RentalServiceDisplay =='5':
            sys.exit()
        else:
            print('1~5까지의 숫자를 입력 하세요^_^')

# 생성자
def __init__(self):
    while True:
        self.display()

# 회원 서비스 =======================================================================
def memberService(self):
    while True:
        # 회원 등록, 수정, 삭제, 리스트 보기
        memberMenu =input('''
================================================================
1.회원등록 2.회원정보 수정 3.삭제 4.회원 리스트 보기 5.뒤로가기
================================================================
>>>''')
        while True:
            memberChoice = input(memberMenu)
            # member create/insert
            if memberChoice =='1':
                self.insertMember()
            # member update    
            elif memberChoice == '2':
                self.updateMember()
            # member delete
            elif memberChoice == '3':
                self.deleteMember()
            # member select
            elif memberChoice == '4':
               self.selectMember()
            elif memberChoice == '5':
                break

# create member table
def insertMember(self):
    con = sqlite3.connect('python_basic/04_project/member.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS MEMBER(
        MID TEXT PRIMARY KEY, MNAME TEXT, TEL TEXT, BIRTH TEXT
    )''')

    # member insert
    con = sqlite3.connect('python_basic/04_project/member.db')
    cur = con.cursor()
    # mid 자동으로 생성되게 수정할것 -> procedure 사용? select max(mid)+1 이런식으로 넣는거 찾아볼 것
    mid = input('ID를 입력하세요>>>')
    mname = input('회원 이름을 입력하세요>>>')
    tel = input('전화번호를 입력하세요 >>>')
    birth = input('생년월일 6자리를 입력하세요>>>')
    sql = 'INSERT INTO MEMBER VALUES(?,?,?,?)'

    cur.execute(sql,(mid,mname,tel,birth))
    con.commit()
    print(f'{mname} 회원 정보가 등록되었습니다.')
    con.close()

# update member
def updateMember(self):
    con = sqlite3.connect('python_basic/04_project/member.db')
    cur = con.cursor()

    cur.execute('SELECT MID, MNAME, TEL, BIRTH FROM MEMBER')
    data = cur.fetchall()
    for i in data:
        print(i)

    # 이거 다시 만들기
    try:
        mid = cur.execute('')
        col = input('수정할 컬럼을 선택하세요 (mname, tel, birth)>>>')
        updatedVal = input('수정할 내용을 입력하세요 >>>')
        sql = f'UPDATE MEMBER SET ? = ? WHERE MID = ?'
        cur.execute(sql,(col, updatedVal, mid))

    except sqlite3.Error as e:
        print(e)
    else:
        con.commit()
        con.close()
        print('수정 완료~!')

# delete member
def deleteMember(self):
    con = sqlite3.connect('python_basic/04_project/member.db')
    cur = con.cursor()

    cur.execute('SELECT MID, MNAME, TEL, BIRTH FROM MEMBER')
    data = cur.fetchall()
    for i in data:
        print(i)

    mid = input('삭제하시려는 회원의 아이디를 입력하세요 >>>')
    sql = 'DELETE FROM MEMBER WHERE MID = ?'
    cur.execute(sql,(mid,))

    con.commit()
    con.close()
    print('삭제 완!')

# select member
def selectMember(self):
    con = sqlite3.connect('python_basic/04_project/member.db')
    cur = con.cursor()

    cur.execute('SELECT MID, MNAME, TEL, BIRTH FROM MEMBER')
    data = cur.fetchall()
    for i in data:
        print(i)

# 도서 서비스 =======================================================================
def bookService(self):
    BookMenu =input('''
================================================================
1.도서등록 2.도서정보 수정 3.삭제 4.도서 리스트 보기 5.뒤로가기
================================================================
>>>''')
    while True:
        bookChoice = input(BookMenu)
        # book insert
        if bookChoice =='1':
            self.insertBooks()
        # book update
        elif bookChoice =='2':
            self.updateBooks()
        # book delete
        elif bookChoice =='3':
            self.deleteBooks()
        # book select
        elif bookChoice =='4':
            self.selectBooks()
        elif bookChoice =='5':
            break

# create table books
def insertBooks(self):
    con = sqlite3.connect('python_basic/04_project/book.db')
    cur = con.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS BOOKS(
        BID TEXT PRIMARY KEY, BNAME TEXT, AUTHOR TEXT, PUBLISHER TEXT 
    )
    ''')

    # book insert
    bid = input('책 아이디를 입력하세요 >>>')
    bname = input('책 제목을 입력하세요 >>>')
    author = input('저자를 입력하세요 >>>')
    publisher = input('출판사를 입력하세요 >>>')
    sql = 'INSERT INTO BOOKS VALUES(?,?,?,?)'

    cur.execute(sql,(bid,bname,author,publisher))

    con.commit()
    con.close()
    print(f'{bname} 정보가 입력되었습니다.')

# update books
def updateBooks(self):
    con = sqlite3.connect('python_basic/04_project/book.db')
    cur = con.cursor()

    bid = input('수정하실 책 아이디를 입력하세요 >>>')
    col = input('수정하실 컬럼을 선택하세요(bname, author, publisher) >>>')
    updatedVal = input('수정할 내용을 입력하세요 >>>')

    sql = f'UPDATE BOOKS SET {col} = ? WHERE BID = ?'
    cur.execute(sql, (bid, updatedVal))

    con.commit()
    con.close()
    print('수정 완료!')

# delete books
def deleteBooks(self):
    con = sqlite3.connect('python_basic/04_project/book.db')
    cur = con.cursor()

    cur.execute('SELECT BID, BNAME, AUTHOR, PUBLISHER FROM BOOKS')
    data = cur.fetchall()
    for i in data:
        print(i)
    
    bid = input('도서 아이디를 입력하세요 >>>')
    sql = 'DELETE FROM BOOKS WHERE BID = ?'
    cur.execute(sql, (bid,))
    print('삭제 완료~')
    con.commit()
    con.close()

# select books
def selectBooks(self):
    con = sqlite3.connect('python_basic/04_project/book.db')
    cur = con.cursor()

    cur.execute('SELECT BID, BNAME, AUTHOR, PUBLISHER FROM BOOKS')
    data = cur.fetchall()
    for i in data:
        print(i)


# 대출 서비스 =======================================================================
# Rent insert
def insertRent(self):
    con = sqlite3.connect('python_basic/04_project/rent.db')
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS RENT(
        rid integer,
        mid integer,
        bid integer,
        rday date
    )
    ''')
    con.commit()
    con.close()

    con = sqlite3.connect('python_basic/04_project/rent.db')
    cur = con.cursor() 
    
    sql = 'INSERT INTO RENT VALUES(?,?,?,?)'
    rid = input('대출아이디를 입력하세요 >>>')
    mid = input('회원아이디를 입력하세요 >>>')
    bid = input('도서아이디를 입력하세요 >>>')
    rday = cur.execute("SELECT date('now','start of month','+14 day')")
    cur.execute(sql,(rid,mid,bid,rday))

bookRental()
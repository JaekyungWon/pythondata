import sqlite3

from matplotlib.pyplot import title

# table 만드는 함수
def create_table():
    conn = sqlite3.connect('python_basic/03_db/my_book.db')
    cur = conn.cursor()
    cur.execute('''
    create table if not exists books(
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommend integer
    )
    ''')
    conn.commit()
    conn.close()

# insert 하는 함수
def insert_book():
    #책 이름, 출판일, 출판사, 페이지 수, 좋아요 수 
    conn = sqlite3.connect('python_basic/03_db/my_book.db')
    cur = conn.cursor()

    sql = 'insert into books values(?,?,?,?,?)'

    title = input('책 제목을 입력하세요 >>>')
    published_date = input('출판일을 입력하세요 >>>')
    publisher = input('출판사를 입력하세요 >>>')
    pages = input('페이지 수를 입력하세요 >>>')
    recommend = input('좋아요 수를 입력하세요 >>>')
    bookInfo = (title, published_date, publisher, pages, recommend)

    cur.execute(sql,bookInfo)
    conn.commit()
    conn.close()

# list보는 함수
def list_book():
    conn = sqlite3.connect('python_basic/03_db/my_book.db')
    cur = conn.cursor()

    cur.execute('select * from books')
    data = cur.fetchall()
    for i in data:
        print(f'책 제목 : {i[0]} / 출판일 : {i[1]} / 출판사 : {i[2]} / 총 페이지 수 : {i[3]} / 좋아요 수 : {i[4]}')
    conn.close()

# update하는 함수
def update_book():
    conn = sqlite3.connect('python_basic/03_db/my_book.db')
    cur = conn.cursor()
    title = input('수정할 책 제목을 입력하세요 >>>')
    col = input('수정할 항목(title, published_date, publisher, pages, recommend)을 입력하세요 >>>')
    updatedVal = input('수정할 내용을 입력하세요 >>>')
    sql = f'update books set {col} = ? where title = ?'

    cur.execute(sql,(updatedVal,title))
    print('수정 완')
    conn.commit()
    conn.close()

# delete 함수
def delete_book():
    conn = sqlite3.connect('python_basic/03_db/my_book.db')
    cur = conn.cursor()
    
    title = input('삭제할 책 이름을 입력하세요 >>>')
    sql = 'delete from books where title like "%" || ? || "%"'
    cur.execute(sql,(title,))
    print('데이터가 삭제 되었습니다!')

    conn.commit()
    conn.close()

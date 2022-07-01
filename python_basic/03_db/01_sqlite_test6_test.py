import sqlite_test6 as st, sys

st.create_table()
while True:
    menu = input('''
====================================================
1.책 정보 입력  2.수정  3.삭제  4.리스트보기  5.종료
====================================================
>>>''')
    if menu == '1':
        st.insert_book()
    elif menu == '2':
        st.update_book()
    elif menu == '3':
        st.delete_book()
    elif menu =='4':
        st.list_book()
    elif menu =='5':
        sys.exit()
    else:
        print('1~5까지의 숫자를 입력하세요')
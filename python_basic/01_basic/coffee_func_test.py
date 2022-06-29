import coffee_func as cf

item = cf.data_load('python_basic\\01_basic\item.json')
menu_display = '''
--------------------------------------------------------
1.커피자판기   2.메뉴추가  3.메뉴삭제  4.메뉴목록  5.종료
--------------------------------------------------------
>>> '''

while True:
    menu = input(menu_display)
    if menu == '1':
        cf.coffee_machine(item)
    elif menu =='2':
        cf.add_menu(item)
    elif menu == '3':
        cf.del_menu(item)
    elif menu =='4':
        cf.menu_list(item)
    elif menu == '5':
        cf.data_save('python_basic\\01_basic\item.json', item)
        print('종료~')
        break
    else:
        print('메뉴를 잘못 선택하셨습니다.')
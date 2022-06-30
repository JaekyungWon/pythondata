import sys, json
class CoffeeMachine:

    # 커피자판기
    def coffee_machine(self):
        while True:
            for k,v in self.item.items():
                print(f'{k}:{v:,}원',end=' ')
            print()
            choice = input('메뉴선택(종료:enter) >>>')
            if choice == '':
                break
            # 숫자가 아니면 다시 입력하도록
            money = ''
            while not money.isdigit():
                money = input('금액 투입 >>>')
            money = int(money)
            
            if choice in self.item.keys(): 
                if money >= self.item[choice]:
                    money -= self.item[choice]
                    print(f'{choice} 서비스 합니다. 거스름돈은 {money}')
                else:
                    print('금액이 부족합니다.' f'{money}원 반환합니다.')
            else:
                print('해당 메뉴가 없습니다.')

    # 메뉴 추가
    def add_menu(self):
        menu_name = input('메뉴명 >>> ')
        menu_price = ''

        while not menu_price.isdigit():
            menu_price = input('메뉴가격 >>> ')
        menu_price = int(menu_price)
        
        if menu_name in self.item.keys():
            print(f'{menu_name} 메뉴가 있습니다. 수정합니다. ')
        else:
            print(f'{menu_name} 메뉴를 추가합니다.')
        self.item[menu_name] = menu_price
        print(self.item)

    # 메뉴 삭제
    def del_menu(self):
        menu_name = input('삭제하려는 메뉴명 >>>')
        if menu_name in self.item.keys():
            print(f'{menu_name} 메뉴를 삭제합니다.')
            del self.item[menu_name]
        else:
            print(f'{menu_name} 메뉴가 없습니다.')
        print(self.item)        

    # 메뉴 목록
    def menu_list(self):
        menu_1 = input('1.이름순 2.가격순 >>> ')
        if menu_1 == '1':
            for k,v in sorted(self.item.items(),key=lambda x : x[0]):
                print(f'{k:25} : {v:10,}원')
        elif menu_1 == '2':
            for k,v in sorted(self.item.items(),key=lambda x : x[1]):
                print(f'{k:25} : {v:10,}원')

    # 파일경로 로드
    def data_load(self,path):
        f = open(path,'r')
        data = json.load(f)
        f.close()
        return data
        
    # 데이터 저장
    def data_save(self,path, data):
        f = open(path,'w')
        json.dump(data,f)
        f.close()

    # 프로그램 시작 화면 디스플레이
    def menu_display(self):
        menu_display = '''
--------------------------------------------------------
1.커피자판기   2.메뉴추가  3.메뉴삭제  4.메뉴목록  5.종료
--------------------------------------------------------
>>> '''
        menu = input(menu_display)
        return menu

    # 프로그램 실행
    def exe(self, menu):
        if menu == '1':
            self.coffee_machine()
        elif menu =='2':
            self.add_menu()
        elif menu == '3':
            self.del_menu()
        elif menu =='4':
            self.menu_list()
        elif menu == '5':
            self.data_save('python_basic\\01_basic\item.json', self.item)
            print('종료~')
            sys.exit()
        else:
            print('메뉴를 잘못 선택하셨습니다.')

    # 생성자
    def __init__(self):
        self.item = self.data_load('python_basic\\01_basic\item.json')
        while True:
            self.exe(self.menu_display())    

CoffeeMachine()

    
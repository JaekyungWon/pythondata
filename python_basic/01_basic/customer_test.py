import sys, json, re

class Customer:

    # 파일경로 로드
    def data_load(self,path):
        f = open(path,'r')
        data = json.load(f)
        f.close()
        return data
        
    # 데이터 저장
    def data_save(self,path, data):
        f = open(path,'w')
        json.dump(data,f,indent=True)
        # indent=True하면 데이터가 줄맞춰서 나와서 보기가 편하다
        f.close()

    # 입력 함수
    def inputInfo(self):
        # 이름  
        customer = {}
        customer['name'] = input('이름 >>>')
        # 성별
        while True:
            customer['gender'] = input('성별(M/F) >>>').upper()
            if customer['gender'] in ('M', 'F'):
                break
        # 이메일 -> pk로 쓸 것
        while True:
            p = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}[.](kr|com|org|net)$')
            while True:
                customer['email'] = input('이메일 >>>')
                result = p.match(customer['email'])
                if result:
                    break
                else:
                    print('정확한 이메일을 입력하세요')
            check = 0
            for i in self.custlist:
                if customer['email'] == i['email']:
                    check =1
            if check ==0:
                break
            else:
                print('중복된 이메일이 있습니다')
        # 출생연도
        while True:
            customer['birth'] = input('출생연도 4자리>>>')
            if len(customer['birth']) == 4 and customer['birth'].isdigit():
                break

        # custlist에 입력 받은 값 추가
        self.custlist.append(customer)

        # 페이지 +1
        self.page = len(self.custlist) -1
        print(customer)
        print(self.custlist)

    # 조회 함수 C
    def showListC(self):
        if self.page < 0:
            print('입력된 정보가 없습니다.')
        else:
            print(f'현재 페이지는 {self.page+1}번째 페이지입니다.')
            print(self.custlist[self.page])

    # 조회 함수 P
    def showListP(self):
        if self.page <= 0:
            print('첫번째 페이지입니다. 이전 페이지 이동 불가~!')
        else:
            self.page -= 1
            print(f'현재 페이지는 {self.page+1}번째 페이지입니다.')
            print(self.custlist[self.page])
        print(self.page)
        return self.page # -1한 변경된 page값 return 해줘야됨


    # 조회 함수 N
    def showListN(self):
        if self.page >= len(self.custlist) -1:
            print('마지막 페이지입니다 ^^ 다음 페이지 없음~!')
        else:
            self.page +=1
            print(f'현재 페이지는 {self.page+1}번째 페이지입니다.')
            print(self.custlist[self.page])
        print(self.page)
        return self.page

    # 삭제 함수
    def delInfo(self):
        print(self.custlist)
        email = input('삭제하려는 이메일을 입력하세요 >>>')
        delok = 0
        for i in range(len(self.custlist)):
            if email == self.custlist[i]['email']:
                print('{} 고객님의 정보가 삭제됩니다'.format(self.custlist[i]['name']))
                del self.custlist[i]
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 고객입니다.')
        print(self.custlist)

    # 수정 함수
    def upInfo(self):
        while True:
            email = input('수정하려는 이메일을 입력하세요 >>>')
            idx = -1
            for i in range(len(self.custlist)):
                if email == self.custlist[i]['email']:
                    idx = i
                    break
            if idx == -1:
                print('등록되지 않은 이메일입니다.')
                break
            choice1 = input('''
            다음 중 수정할 항목을 선택하세요(name, gender, birth) >>>
            ''')
            self.custlist[idx][choice1] = input('수정 할 {} 를 입력하세요 >>>'.format(choice1))
            print(self.custlist)
            break

    def exe(self):
        choice=input('''
==========================================================================
                        고객 정보 관리 프로그램 
==========================================================================
I - 고객 정보 입력  C - 현재 고객 정보 조회    P - 이전 고객 정보 조회
N - 다음 고객 정보 조회  U - 고객 정보 수정   D - 고객 정보 삭제  Q - 종료
==========================================================================
''').upper()
        # 입력
        if choice=="I":
            self.inputInfo()
        # 조회(C, P, N)   
        elif choice=="C": 
            self.showListC()
        elif choice == 'P':
            self.showListP()
        elif choice == 'N':
            self.showListN()
        # 삭제
        elif choice=='D':
            self.delInfo()
        # 수정
        elif choice=="U": 
            self.upInfo()
        # 정보 저장하고 종료
        elif choice=="Q":
            self.data_save('python_basic\\01_basic\custlist.json',self.custlist)
            print('종료~')
            sys.exit()

    def __init__(self):
        self.custlist=self.data_load('python_basic\\01_basic\custlist.json')
        self.page = len(self.custlist)-1
        while True:
            self.exe()

Customer()


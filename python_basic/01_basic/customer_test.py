import re, customer_test_func as ct
custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'ashdkl@gildong.com', 'birth': '2000'},
          {'name': '미미', 'gender': 'F', 'email': 'asdasdasd@naver.com', 'birth': '1995'},
          {'name': 'MOMO', 'gender': 'F', 'email': 'momo198@gmail.com', 'birth': '2004'}]
# custlist = []
page = len(custlist)-1

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()  

    # 입력
    if choice=="I":
       ct.inputInfo(custlist)
        
    # 조회(C, P, N)   
    elif choice=="C": 
       ct.showListC(custlist, page)
    elif choice == 'P':
        ct.showListP(custlist, page)
    elif choice == 'N':
        ct.showListN(custlist, page)
    # 삭제
    elif choice=='D':
        ct.delInfo(custlist)
    # 수정
    elif choice=="U": 
        ct.upInfo(custlist)
    elif choice=="Q":
        break


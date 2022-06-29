import re

# 입력 함수
def inputInfo(custlist):
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
        for i in custlist:
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
    custlist.append(customer)

    # 페이지 +1
    page = len(custlist) -1
    print(customer)
    print(custlist)

# 조회 함수 C
def showListC(custlist, page):
    if page < 0:
        print('입력된 정보가 없습니다.')
    else:
        print(f'현재 페이지는 {page+1}번째 페이지입니다.')
    print(custlist)

# 조회 함수 P
def showListP(custlist, page):
    if page <= 0:
        print('첫번째 페이지입니다. 이전 페이지 이동 불가~!')
    else:
        page -= 1
        print(f'현재 페이지는 {page+1}번째 페이지입니다.')
        print(custlist[page])
    print(page)

# 조회 함수 N
def showListN(custlist, page):
    if page >= len(custlist) -1:
        print('마지막 페이지입니다 ^^ 다음 페이지 없음~!')
    else:
        page +=1
        print(f'현재 페이지는 {page+1}번째 페이지입니다.')
        print(custlist[page])
    print(page)

# 삭제 함수
def delInfo(custlist):
    print(custlist)
    email = input('삭제하려는 이메일을 입력하세요 >>>')
    delok = 0
    for i in range(len(custlist)):
        if email == custlist[i]['email']:
            print('{} 고객님의 정보가 삭제됩니다'.format(custlist[i]['name']))
            del custlist[i]
            delok = 1
            break
    if delok == 0:
        print('등록되지 않은 고객입니다.')
    print(custlist)

# 수정 함수
def upInfo(custlist):
    while True:
        email = input('수정하려는 이메일을 입력하세요 >>>')
        idx = -1
        for i in range(len(custlist)):
            if email == custlist[i]['email']:
                idx = i
                break
        if idx == -1:
            print('등록되지 않은 이메일입니다.')
            break
        choice1 = input('''
        다음 중 수정할 항목을 선택하세요(name, gender, birth) >>>
        ''')
        custlist[idx][choice1] = input('수정 할 {} 를 입력하세요 >>>'.format(choice1))
        print(custlist)
        break
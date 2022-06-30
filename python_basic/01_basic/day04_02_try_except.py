# 예외처리
try:
    value1 = int(input('첫번째 값을 입력 >>>'))
    value2 = int(input('두번째 값을 입력 >>>'))
    print(value1/value2)
except (ZeroDivisionError, ValueError) as e:
    print(e)
except: #종류 모르는 에러면 이렇게 적어도 됨
    print('오류')
    # pass : 오류 처리 안하고 넘어가려면 pass쓰면 된다
else:   #try, except, else도 마지막에 쓸 수 있다
    print('메롱')


# 이렇게 일부러 에러를 발생시킬 수 있다
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass    #이렇게 쓰면 에러가 발생@~@~
    # def fly(self): print('독수리')   : 이렇게 쓰면 제대로 구동
eagle = Eagle()
eagle.fly()

# 예외를 만들어서 쓸 수도 있음
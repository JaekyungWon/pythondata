# 숫자 맞추기 게임

# 컴퓨터가 두 수의 사칙 연산 문제를 내면 맞추는 게임
# 이 때 두 수와 연산자는 랜덤으로 선택된다. 나누기의 경우 소수 이하 값은 정수로 변경해서 처리한다.
# 문제는 종료를 선택할 때 까지 반복된다.
# 종료 시 맞춘 문제 수/ 총 문제수를 출력한다.

# random.randint(start, end)
# random.choice()
# 를 이용할 것

import random
class math:
    def game(self):
        total = 0   #총 문제 수
        hit = 0     #맞춘 문제 수
        while True:
            menu = input('1. 문제보기 2.종료 >>>')
            if menu == '1':
                num1 = random.randint(1, 100)
                num2 = random.randint(1, 100)
                operator = ['+','-','*','/']
                calOperator = random.choice(operator)
                quiz = str(num1) + calOperator + str(num2)

                print(quiz)
                answer = int(input('정답을 입력하세요 >>>'))
                total +=1
                if answer == int(eval(quiz)):
                    print('정답입니당')
                    hit +=1
                else:
                    print('땡!!!!')

            elif menu == '2':
                print(f'맞춘 문제 수:{hit} / 전체 문제 수{total}')
                break
            else:
                print('1이나 2를 입력하세요')
            
    def __init__(self):
        self.game()

math()

# eval() 
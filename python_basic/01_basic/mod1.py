def add(a,b):
    return a+b
print(__name__)

# import 해서 실행하면 파일명만 실행된다. 자기가 실행하면 print해준다
if __name__ == '__main__':
    print(add(2,3))
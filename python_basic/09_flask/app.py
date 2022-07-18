from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# 호출할 때 주소 값
@app.route('/')
# '/' 호출 했을 때 동작할 함수
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    return 'user 호출'

@app.route('/user/<username>/<int:age>')
def user_1(username,age):   #넘어오는 값 받을 수 있게 (변수) 선언하기
    # return username     #type : 설정 안하면 string. int, float, path도 가능
    return f'{username}고객님의 나이는 {age+1}살 입니다.'

@app.route('/customer')
def customer():
    print('user:',request.args.get('user'))
    print('age:',request.args.get('age'))
    return "customer 호출"

@app.route('/login', methods=['GET', 'POST'])
def login():
    # get방식 : 입력 값 가지고 올 때
    if request.method == 'GET':
        return render_template('form_input.html')
    # post방식 : 입력 값 받아서 넘겨줄 때
    else:
        # return f"Login : {request.form['username']} {request.form['password']}"
        return render_template('form_result.html', result=request.form)

# 파일업로드
@app.route('/fileupload', methods=['GET', 'POST'])
def fileupload():
    if request.method == 'GET':
        return render_template('fileupload.html')
    else:   #파일 저장할 경로 지정해야됨
        f = request.files['file']
        path= os.path.dirname(__file__)+'/upload/'+f.filename
        print(path)
        # 파일 저장하기
        f.save(path)

        return redirect('/')

if __name__ == '__main__':
    # 동작시키기
    app.run(host="0.0.0.0", port=80, debug=True)
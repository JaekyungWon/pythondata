from flask import Flask, request, redirect, render_template
import os, sqlite3

# 바로 호출 되면 name, 아니면 파일 이름이 들어간다
app = Flask(__name__)

# DB읽어오는 작업
path = os.path.dirname(__file__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inputform', methods=['GET', 'POST'])
def inputform():
    if request.method == 'GET':
        return render_template('inputform.html')
    else:
        conn = sqlite3.connect(path + '/customer.db')
        cur = conn.cursor()
        cur.execute('''create table if not exists customer
                        (name text,
                        email text,
                        tel text,
                        address text,
                        gender text)''')
        conn.commit()
        data = [request.form['name'],request.form['email'],request.form['tel'],request.form['address'],request.form['gender']]

        cur.execute('insert into customer values(?,?,?,?,?)', data)
        conn.commit()
        conn.close()

        # DB에 데이터 입력하고 루트로 되돌아가기
        return redirect('/')
@app.route('/customerlist')
def customerlist():
    conn = sqlite3.connect(path + '/customer.db')
    cur = conn.cursor()
    cur.execute('select * from customer order by name')
    data = cur.fetchall()
    return render_template('customerlist.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=80) 
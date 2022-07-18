from flask import Flask, request, redirect, render_template
import os, sqlite3

app = Flask(__name__)
path = os.path.dirname(__file__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inputshop', methods=['GET','POST'])
def inputshop():
    if request.method == 'GET':
        return render_template('inputshop.html')
    else:
        con = sqlite3.connect(path+'/shoppinglist.db')
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS shoppinglist(ITEM TEXT, PRICE TEXT, SHOP TEXT, DATE DATE, WISH TEXT)')
        
        con.commit()
        data = [request.form['item'],request.form['price'],request.form['shop'],request.form['date'],request.form['wish']]

        cur.execute('INSERT INTO shoppinglist VALUES(?,?,?,?,?)', data)
        con.commit()
        con.close()

        return redirect('/')

@app.route('/shoppinglist')
def shoppinglist():
    con = sqlite3.connect(path+'/shoppinglist.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM shoppinglist ORDER BY DATE')
    data = cur.fetchall()
    return render_template('shoppinglist.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=80)   
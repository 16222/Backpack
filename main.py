from flask import Flask, render_template, request, jsonify, abort #importing flask libraries
import sqlite3 #importing sqlite3 libraries
import json #importing json libraries

app = Flask(__name__) #initialising server

@app.route('/', methods=['GET', 'POST'])
def main_page():
    conn = sqlite3.connect('storage.db')
    cur = conn.cursor()
    if request.form:
        print(request.form)
        formlist = dict(request.form)
        print(formlist["add"])
        query = '''INSERT INTO stuff (items)
                   VALUES ({});'''.format(formlist["add"])
        cur.execute(query)
        conn.commit()
    query = 'SELECT * FROM STUFF'
    cur.execute(query)
    results = cur.fetchall()
    return render_template('main.html', page_title = 'Home', results=results)

#@app.route('/add', methods=['POST'])
#def add():
#    i = list(request.form)
#    print(i)
    #conn = sqlite3.connect('storage.db')
    #cur = conn.cursor()
    #query = '''INSERT INTO stuff (items)
    #           Values ({})'''.format(i)
    #cur.execute(query)
    #conn.commit()

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port='8080')

from flask import Flask, render_template, request, jsonify, abort, redirect #importing flask libraries
import sqlite3 #importing sqlite3 libraries
import json #importing json libraries
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #initialising server
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///storage.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class stuff(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    data = db.Column(db.String(80), nullable=False)

db.create_all()

@app.route('/', methods=['GET', 'POST'])
def main_page():
    a = [x.__dict__ for x in stuff.query.all()]
    return render_template('main.html', page_title = 'Home', data=a)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.form:
        formlist = dict(request.form)
        a = stuff()
        a.data = formlist['add']
        print(a.data)
        db.session.add(a)
        db.session.commit()
    return redirect('/')

@app.route('/remove', methods=['POST'])
def remove():
    if request.form:
        i = list(request.form)
        i[0] = json.loads(i[0])
        i = dict(i[0])
        print(i)
        a = stuff.query.filter_by(id=i["0"]).first()
        db.session.delete(a)
        db.session.commit()
    return '1'

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port='8080')

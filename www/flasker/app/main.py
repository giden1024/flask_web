#!/usr/bin/env python
# encoding: utf-8
'''
@author: mark
@file: main.py
@time: 2019/6/3 11:18
@desc:
'''

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy
import click
from .model import User,Movies
import os,pymysql
from flask import Blueprint
main = Blueprint(name="main",import_name=__name__)


movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]



db.drop_all()
db.create_all()

user01 = User(name='admin')

db.session.add(user01)
for mo in movies:
    mov = Movies(title=mo['title'],year=mo['year'])
    db.session.add(mov)

db.session.commit()
@app.route('/')
def show_entries():
    # cur = g.db.execute('select title,text from entries order by desc')
    # entries = [dict(title=row[0],text=row[1]) for row in cur.fetchall()]
        return render_template("basic.html",user="abs",movies=movies)

@app.route('/add',methods=['POST'])
def add_entyr():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries(title,text) values (?,?) ',[request.form['title'],request.form['text']])
    g.db.commit()

    flash("New entry was successfully posted!")
    return redirect(url_for('show_entries'))

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error == 'Invalid username'
        elif request.form['password'] != app.config["PASSWORD"]:
            error == 'Invalid password'
        else:
            session['logged_in'] = True
            flash("you were logged in")
            return redirect(url_for('show_entries'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('login_in',None)
    flash('you were logged out')
    return redirect(url_for('show_entries'))

if __name__ == "__main__":

    app.run(debug=True)
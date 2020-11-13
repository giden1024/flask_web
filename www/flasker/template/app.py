#!/usr/bin/env python
# encoding: utf-8
'''
@author: mayuyang
@time: 2020/7/12 17:10
@desc:
'''

from flask import Flask,render_template,redirect,url_for,flash

app = Flask(__name__)
app.secret_key = 'Secret String'

user = {"username": "testuser", "bio": "A boy who lives movie and music."}

movies = [{"name": "My Neighbor Totoro", "year": "1998"},
          {"name": "Three color trilogy", "year": "1993"},
          {"name": "Forrest Gump", "year": "1994"},
          {"name": "Perfect Blue", "year": "1997"}
          ]


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html',user=user,movies = movies)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/flash')
def just_flash():
    flash(u'this is flash message.')
    return redirect(url_for('index'))
#!/usr/bin/env python
# encoding: utf-8
'''
@author: mayuyang
@time: 2020/7/17 10:09
@desc:
'''
from flask import Flask,render_template,url_for
from form.forms import LoginForm
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/basic',methods=['GET','POST'])
def basic():
    form = LoginForm()
    return render_template("basic.html",form=form)


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')


@app.route('/basic2',methods=['GET','POST'])
def basic2():
    form = LoginForm()
    return render_template("basic2.html",form=form)


@app.route('/macros')
def macros():
    return render_template('macros.html')
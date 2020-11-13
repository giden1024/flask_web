#!/usr/bin/env python
# encoding: utf-8
'''
@author: mayuyang
@time: 2020/7/8 19:48
@desc:
'''
import json
from flask import Flask, request, redirect, url_for, abort, make_response,session,g,current_app

app = Flask(__name__)


# @app.route('/')
# def index():
#     return '<h1>index page</h1>'


@app.route('/hello/<name>')
def forname(name):
    return '<h1>hello,%s!</h1>' % name


@app.route('/hi')
def hi():
    name = request.args.get('name', 'Flask')
    return '<h1>hello,%s!</h1>' % name


@app.route('/another')
def another():
    return '', 302, {'Location': 'https://www.bing.com'}


@app.route('/another1')
def another1():
    return redirect("http://www.bing.com")


@app.route('/another2')
def another2():
    return redirect(url_for('another'))


@app.route('/404')
def not_found():
    abort(404)


@app.route('/res')
def resp():
    response = make_response("hello,this is response.")
    response.mimetype = 'text/plain'
    return response


@app.route('/foo')
def foo():
    data = {
        "id": 1,
        "name": "new",
        "age": 14
    }
    response = make_response(json.dumps(data))
    response.mimetype = 'text/plain'
    return response


app.secret_key = 'secret key'


@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('auth'))


@app.route('/')
@app.route('/auth')
def auth():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name','testName')
        response = '<h1>Hello,%s</h1>'%name
    if 'logged_in' in session:
        response += '[Authenticated]'
    else:
        response += '[Not Authenticated]'
    print(session)
    return response


@app.route('/test')
def test():
    name = request.args.get('name','testName')
    s = session.get('')




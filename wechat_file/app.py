#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/10/16 17:29
@desc:
"""
from flask import Flask,url_for,render_template,request,redirect,abort,session,escape,flash

app = Flask(__name__)

app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

# @app.route("/")
# def main():
#     render_template("base.html")

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/login",methods=['GET','POST'])
def login():
    error = None
    if request.method == "POST":
        if request.form['username'] == "shiyanlou" and request.form['password'] == "shiyanlou":
            session['username'] = "shiyanlou"
            flash("登录成功！")
            return redirect(url_for('index'))
        else:
            flash("登录失败！")
            session['username'] = None
            return redirect(url_for('index'))
    return render_template("login.html",error=error)


@app.route("/logout")
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))


@app.route("/")
def main():
    abort(404)


@app.route("/hello")
@app.route('/hello/<username>')
def hello(username=None):
    return render_template('hello.html',username=username)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),200


@app.route("/username/<username>")
def user(username):
    return "hello,%s" % username


@app.route("/id/<int:sid>")
def show_id(sid):
    return "this is %d" % sid


@app.route("/path/<path:spath>")
def get_path(spath):
    return "path is %s" % spath


@app.route("/sum/<int:num1>/<int:num2>")
def sum(num1,num2):
    return "%s与%s的和是%d"%(num1,num2,int(num1)+int(num2))


@app.route("/upload",methods=['GET','POST'])
def upload(file):
    if request.method == 'POST':
        f = request.files['file']


if __name__ == "__main__":
    app.run(debug=True)
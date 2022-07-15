#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/10/22 16:53
@desc:
"""
import sqlite3,os
from image import get_captcha

from flask import Flask,render_template,g,flash,\
    request,session,abort,redirect,url_for

# 配置项
DATABASE = os.path.abspath(os.getcwd()) + r'/tmp/flasker.db'
ENV = 'development'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = '123456'
FLASK_APP = 'app.py'

app = Flask(__name__)
app.config.from_object(__name__) # 读取当前所有文件下的大写变量作为配置项。from_object() 将会寻找给定的对象(如果它是一个字符串，则会导入它)，搜寻里面定义的全部大写的变量。


def db_conn():  # 数据库配置地址
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_conn():
    g.conn = db_conn()


def init_db():
    with db_conn() as conn:
        with app.open_resource('schema.sql') as f:
            conn.cursor().executescript(f.read().decode())
    conn.commit()


@app.teardown_request
def teardown(exception):
    g.conn.close()


@app.route("/")
@app.route("/show_entries")
def show_entries():
    cursor = g.conn.execute('select title,text from entries order by id DESC ')
    entries = [dict(title=row[0],text=row[1]) for row in cursor.fetchall()]
    return render_template('show_entries.html')


@app.route("/code")
def get_code():
    session['cap']


@app.route("/add_entry",methods=['POST'])
def add_entry():
    if not session.get('login'):
        abort(401)
    g.conn.execute('INSERT INTO entries(title,text) values (?,?)',[request.form.get('title'),request.form.get('text')])
    g.conn.commit()
    flash("添加成功")
    return redirect(url_for('show_entries'))


@app.route("/login",methods=['GET','POST'])
def login():
    error = None
    captcha = get_captcha("static/img/", "cap.jpeg")
    session['cap'] = captcha
    print(captcha)
    if request.method == "POST":

        if request.form.get("captcha") != session['cap']:
            print(request.form.get("captcha") + "!")
            print(session['cap']+"!")
            flash("验证码错误")
        elif request.form.get('username') == app.config.get('USERNAME') and request.form.get('password') == app.config.get('PASSWORD'):
            session['login'] = True
            flash("登录成功")
            return redirect(url_for("show_entries"))
        else:
            flash("登录失败，请检查用户名或者密码。")
            # session.pop("login")
    print(captcha)
    return render_template("login.html",error=error)


@app.route("/logout")
def logout():
    session.pop("login")
    flash("您已经成功退出")
    return redirect(url_for("show_entries"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),200


@app.route("/new")
def new():
    return redirect(url_for("show_entries"))



if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.2")



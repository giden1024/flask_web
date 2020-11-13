#!/usr/bin/env python
# encoding: utf-8
'''
@author: mark
@file: model.py
@time: 2019/6/6 15:53
@desc:
'''

from . import db, login_manager



# @main.cli.command()  # 注册为命令
# @click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
# def initdb(drop):
#     """Initialize the database."""
#     if drop:  # 判断是否输入了选项
#         db.drop_all()
#     db.create_all()
#     click.echo('Initialized database.')  # 输出提示信息


class User(db.Model):
    __tablename__ = 'movieuser'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))


class Movies(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份



#!/usr/bin/env python
# encoding: utf-8
'''
@author: mark
@file: config.py
@time: 2019/6/3 15:25
@desc:
'''

import os
import logging

class Config:
    DEBUG = True
    SECRET_KEY= '123456'
    # ORM底层所访问数据库URI
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/testweb?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 当关闭数据库是否自动提交事务
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 是否追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True


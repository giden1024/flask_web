#!/usr/bin/env python
# encoding: utf-8
'''
@author: mark
@file: __init__.py.py
@time: 2019/6/6 16:24
@desc:
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    # app.config.from_object(config[config_name])

    return app
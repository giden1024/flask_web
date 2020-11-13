#!/usr/bin/env python
# encoding: utf-8
'''
@author: mark
@file: app.py
@time: 2019/6/3 10:43
@desc:
'''
# all the imports
# import os
# import sqlite3
# from flask import Flask, request, session, g, redirect, url_for, abort, \
#      render_template, flash
#
# app = Flask(__name__)
#
# def connect_db():
#     """Connects to the specific database."""
#     rv = sqlite3.connect(app.config['DATABASE'])
#     rv.row_factory = sqlite3.Row
#     return rv
# app.config.from_envvar("FLASKR_SETTINGS", silent=True)
#
#
# def init_db():
#     with app.app_context():
#         db = get_db()
#         with app.open_resource('schema.sql', mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()
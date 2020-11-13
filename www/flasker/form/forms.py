#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/7/17 10:01
@desc:
"""

from wtforms import Form,StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,InputRequired
from flask_wtf import FlaskForm

def my_length(form,field):
    if len(form.data) > 50:
        raise ValueError('Field must be more the 50 characters')

class LoginForm(Form):
    username = StringField('Username',render_kw={'placeholder':'Your Username'},validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),my_length])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')



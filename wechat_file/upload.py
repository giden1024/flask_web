#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/10/20 14:32
@desc:
"""
import os
from flask import Flask,render_template
from flask import request
from werkzeug.utils import secure_filename

path = os.path.dirname(__file__)
UPLOAD_FILE = path + "/file"
ALLOW_EXTENSIONS = ['txt','jpg','gif','jepg','pdf','png']

app = Flask(__name__)
app.config['UPLOAD_FILE'] = UPLOAD_FILE


def allowed(filename):
    return '' in filename and filename.split('.')[-1] in ALLOW_EXTENSIONS


@app.route('/login',methods=['GET',"POST"])
def upload_file():

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed(file.filename):
            filename = secure_filename(file.filename)   # 获取上传文件的文件名
            file.save(os.path.join(app.config['UPLOAD_FILE'], filename))   # 保存文件
            return '%s upload success'%filename
        else:
            return '后缀名错误，上传失败！'
    else:
        return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)

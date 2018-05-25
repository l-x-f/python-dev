#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/index', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == '1234':
        return render_template('welcome.html')
    return  render_template('form.html',message='密码或用户名错误')
if __name__ == '__main__':
    app.run()

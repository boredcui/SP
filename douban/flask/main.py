#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-12 15:11:16
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-12 16:17:44
FilePath: \flask\main.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
from flask import Flask

app = Flask(__name__)


# 路由解析，通过用户访问的路径，匹配相应的函数
@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)

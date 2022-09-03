#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-12 15:11:16
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-09-03 22:22:49
FilePath: \SP\douban\flask\main.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''

from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


# 路由解析，通过用户访问的路径，匹配相应的函数
@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/index")
def index():
    # return render_template("index.html")
    return hello()


@app.route("/movie")
def movie():
    datalist = []
    con = sqlite3.connect("./douban/flask/movieTop250.db")
    cur = con.cursor()
    sql = "select * from movie"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie.html",movies = datalist)


@app.route("/music")
def music():
    datalist = []
    con = sqlite3.connect("./douban/flask/musicTop250.db")
    cur = con.cursor()
    sql = "select * from music"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("music.html",musics = datalist)


@app.route("/book")
def book():
    datalist = []
    con = sqlite3.connect("./douban/flask/bookTop250.db")
    cur = con.cursor()
    sql = "select * from book"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("book.html",books = datalist)


@app.route("/score")
def score():
    score1 = []
    num1 = []
    con1 = sqlite3.connect("./douban/flask/bookTop250.db")
    cur1 = con1.cursor()
    sql = "select score,count(score) from book group by score"
    data1 = cur1.execute(sql)
    for item in data1:
        score1.append(item[0])
        num1.append(item[1])
    cur1.close()
    con1.close()
    score2 = []
    num2 = []
    con2 = sqlite3.connect("./douban/flask/movieTop250.db")
    cur2 = con2.cursor()
    sql = "select score,count(score) from movie group by score"
    data2 = cur2.execute(sql)
    for item in data2:
        score2.append(item[0])
        num2.append(item[1])
    cur2.close()
    con2.close()
    score3 = []
    num3 = []
    con3 = sqlite3.connect("./douban/flask/musicTop250.db")
    cur3 = con3.cursor()
    sql = "select score,count(score) from music group by score"
    data3 = cur3.execute(sql)
    for item in data3:
        score3.append(item[0])
        num3.append(item[1])
    cur3.close()
    con3.close()
    return render_template("score.html",score1=score1,num1=num1,score2=score2,num2=num2,score3=score3,num3=num3)


if __name__ == '__main__':
    app.run(debug=True)

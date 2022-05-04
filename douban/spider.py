#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-03 20:27:45
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-04 21:15:42
FilePath: \SP\douban\spider.py
Description: 

Copyright (c) 2022 by boredcui 1637188453@qq.com, All Rights Reserved. 
'''
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则式表达，进行文字匹配
import urllib.request  # 制定URL，获取网页数据
import urllib.error
import xlwt  # 进行excel操作
import sqlite3  # sqlite数据库


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取数据
    datalist = getDate(baseurl)
    savepath = ".\\豆瓣电影TOP250.xls"
    # 3.保存数据
    # saveDate(savepath)
    askURL("https://movie.douban.com/top250?start=")


# 爬取网页
def getDate(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数，10次
        url = baseurl+str(i*25)
        html = askURL(url)  # 保存获取到的网页源码

        # 2.逐一解析数据

    return datalist


# 得到一个指定URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32"
    }  # 用户代理

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 保存数据
def saveDate(savepath):
    print("save")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# coding=utf-8
'''
Author: boredcui 1637188453@qq.com
Date: 2022-05-03 20:27:45
LastEditors: boredcui 1637188453@qq.com
LastEditTime: 2022-05-06 15:30:27
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
    savepath = "./douban/豆瓣电影TOP250.xls"
    # 3.保存数据
    saveDate(datalist, savepath)
    # askURL("https://movie.douban.com/top250?start=")


findLink = re.compile(r'<a href="(.*?)">')  # 创建影片链接正则表达式对象
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # 图片 re.S 让换行符包含在字符内
findTitle = re.compile(r'<span class="title">(.*)</span>')  # 片名
findRating = re.compile(
    r'<span class="rating_num" property="v:average">(.*)</span>')  # 评分
findJudge = re.compile(r'<span>(\d*)人评价</span>')  # 评价人数
findInq = re.compile(r'<span class="inq">(.*)</span>')  # 概况
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)  # 相关内容


# 爬取网页
def getDate(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数，10次
        url = baseurl+str(i*25)
        html = askURL(url)  # 保存获取到的网页源码

        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)#test
            data = []  # 保存一部电影的所有信息
            item = str(item)

            Link = re.findall(findLink, item)[0]  # 通过正则表达式查找影片链接的字符串
            data.append(Link)  # 添加链接

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)  # 添加图片

            titles = re.findall(findTitle, item)
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)  # 添加中文名
                otitle = titles[1].replace("/", "")  # 去掉无关的符号
                data.append(otitle)  # 添加外文名
            else:
                data.append(titles[0])
                data.append(' ')  # 外文名留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)  # 添加评分

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)  # 添加评价人数

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)  # 添加概述
            else:
                data.append(" ")  # 留空

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # strip去掉前后的空格

            datalist.append(data)  # 把处理好的电影信息放入

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
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 保存数据
def saveDate(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影TOP250', cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外文名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, 250):
        print("第%d条" % (i+1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i+1, j, data[j])  # 数据
    book.save(savepath)  # 保存


if __name__ == "__main__":
    main()
    print("爬取完毕")

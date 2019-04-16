# level 1:
# 1、阅读课件，掌握正则表达式的基本用法，常用的方法的使用
# 2、 match 方法和 search 方法的区别？
#     match 从起始位置开始查找，一次匹配
#     search 从任何位置开始查找，一次匹配

# 3、 如何理解贪婪模式和非贪婪模式
#       贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配（*）
#       非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配（？）
import requests
import re
from bs4 import BeautifulSoup
# 案例：爬取内涵吧爬虫（re）
# https://www.neihan8.com/article/index.html
# 正则表达式提取段子标题，url，点赞数，踩数，内容

'''
def crawlDuanzi(pageNums):
    # 网页爬取
    curPage = 1
    while curPage <= pageNums:

        if curPage == 1:
            url = 'https://www.neihan-8.com/article/index.html'
        else:
            url = 'https://www.neihan-8.com/article/index_'+str(curPage)+'.html'

        headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
        respose = requests.get(url,headers=headers)
        html = respose.content.decode()
        #print(html)
        # 数据提取
        pat_item = re.compile(r'<div class="text-column-item box box-790">(.*?<div class="view".*?>.*?</div>)',re.M | re.S)
        ls = pat_item.findall(html)
        print(len(ls))
        pat_title = re.compile(r'<h3>.*?<a.*?>(.*?)</a>',re.M | re.S)
        pat_url = re.compile(r'<h3>.*?<a.*?href="(.*?)"',re.M | re.S)
        pat_support = re.compile(r'<div.*?class="good".*?>(.*?)</div>', re.M | re.S)
        pat_against = re.compile(r'<div.*?class="bad".*?>(.*?)</div>', re.M | re.S)
        pat_views = re.compile(r'<div.*?class="view".*?>(.*?)</div>', re.M | re.S)
        pat_desc = re.compile(r'<div.*?class="desc".*?>(.*?)</div>', re.M | re.S)
        #pat_title = re.compile(r'', re.M | re.S)
        base_url = 'https://www.neihan-8.com/'
        for item in ls:
            #print(item)
            title = pat_title.search(item).group(1).strip()
            print('title:',title)
            url = base_url + pat_url.search(item).group(1).strip()
            print('url:', url)
            suport_nums = pat_support.search(item).group(1).strip()
            print('suport_nums:', suport_nums)
            against_nums = pat_against.search(item).group(1).strip()
            print('against_nums:', against_nums)
            views_nums = pat_views.search(item).group(1).strip()
            print('views_nums:', views_nums)
            desc = pat_desc.search(item).group(1).strip()
            print('desc:', desc)

            print('='*60)

        # 数据存储

        curPage +=1


if __name__ == "__main__":
    nums = int(input('请输入爬取的页数：'))
    crawlDuanzi(nums)

'''

# 案例：中超新闻爬虫(re)
# http://sports.163.com/zc/
# 提取新闻标题，url，关键字，评论数
# 保存到mongodb中
'''
import requests, re, pymongo

def req(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    return response.text

def spider(html):
    div = re.compile('<div class="news_item">(.*?)</span>', re.S)
    div = div.findall(html)
    for d in div:
        print('='*100)
        # print(d)
        a = re.compile('<h3><a href="(.*?)">(.*?)</a></h3>')
        url = a.search(d).group(1)
        title = a.search(d).group(2)
        print('标题：', title)
        print('url:', url)
        gjz = re.compile('<div class="keywords">.*?<a href=".*?">(.*?)</a>.*?<a href=".*?">(.*?)</a>', re.S)
        gjz = ' '.join(gjz.search(d).groups())
        print('关键字：',gjz)
        comment = re.compile('<span class="icon">(\d+)')
        comment = comment.search(d).group(1)
        print('评论数：', comment)

        # 保存数据库
        item = {
            'title':title,
            'url':url,
            'gjz':gjz,
            'comment':comment,
        }
        result = save().insert(item)
        print(result)

def save():
    client = pymongo.MongoClient(host='127.0.0.1', port=27017)
    # 创建数据库
    db = client.text  # 或db = client['text']
    # 创建集合（表）
    p = db.zcxw_spdier  #或p = db['zcxw_spdier']
    return p


if __name__ == '__main__':
    URL = 'http://sports.163.com/zc/'
    html = req(URL)
    spider(html)
'''
# level 2:
# 案例：链家二手房爬虫（re）
# https://sh.lianjia.com/ershoufang/
# 提取标题，链接，单价，总价，基本信息，房源特色信息
# #
# headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                          "(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
# url = 'https://sh.lianjia.com/ershoufang'
# respons = requests.get(url, headers)
# html = respons.text
# print(html)
# BeautifulSoup(html, 'lxml')
# re_all = re.compile(r'<li class="clear LOGCLICKDATA">(.*?)</li>')
# ls = re_all.findall(html, re.M | re.S)
# print(len(ls))

from selenium import webdriver
browser = webdriver.Chrome()







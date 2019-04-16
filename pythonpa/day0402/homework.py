# level 1:
# 阅读课件
#
# 掌握滑动验证码的处理
#
# 豆瓣电影信息爬虫
# https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0
# 爬取电影的名称， url，评分，封面图片

'''
from selenium import webdriver
sta = webdriver.Chrome()
url = 'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
sta.get(url)
namelist = sta.find_elements_by_css_selector('div.list-wp>div>a')
# print(namelist)
for i in namelist:
    n = i.find_element_by_css_selector('p').text
    p = i.find_element_by_css_selector('p>strong').text
    t = i.find_element_by_css_selector('div>img')
    print('电影名称：', n)
    print('电影评分：', p)
    print('封面图片：', )
    print('url:', i.get_attribute('href'))
'''


'''
import requests, json, time
from fake_useragent import UserAgent
def req(url, headers, params):
    respons = requests.get(url, headers=headers, params=params)
    data = json.loads(respons.text)
    # print(data)
    for i in data['subjects']:
        print('电影名称：', i['title'])
        print('电影url：', i['url'])
        print('电影评价：', i['rate'])
        print('图片url：', i['cover'])
        print('='*77)
    while True:
        params['page_start'] += 20
        req(url, headers, params)


if __name__ =='__main__':
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    params = {
        'type': 'movie',
        'tag': '热门',
        'sort': "recommend",
        'page_limit': '20',
        'page_start': 0,
    }
    url = 'https://movie.douban.com/j/search_subjects'
    req(url, headers, params)
    
'''



# 上市公司信息爬虫
# http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback65650&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=1&pageHelp.pageSize=25&pageHelp.pageNo=1&_=1539005987996
# 爬取上海证券交易所网站，
# 获取 A 股上市公司信息，包括公司代码，公司简称， A 股代码，A 股简称,A 股总资本和 A 股流通资本
# 保存到mysql数据库
#
'''
import requests
from bs4 import BeautifulSoup
import json
import re

url = "http://www.sse.com.cn/assortment/stock/list/share/"
data_url = "http://query.sse.com.cn/security/stock/getStockListData2.do?&jsonCallBack=jsonpCallback82088&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=1&pageHelp.pageSize=25&pageHelp.pageNo=1&_=1554291368503"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "Referer": "http://www.sse.com.cn/assortment/stock/list/share/"
}

response = requests.get(data_url, headers=headers)
html = response.text
print(response.text)

# 去除开头的jsonpCallback81793(和结尾的）
a = '{"content":'+response.text[19:-1]+'}'
print(type(a))
"字符串a序列化为字典对象b"
b = json.loads(a)
print(b)
print(type(b))
data = b['content']['pageHelp']['data']
print(len(data))
for item in data:
    print("公司代码：", item['COMPANY_CODE'])
    print("公司简称：", item['COMPANY_ABBR'])
    print("A 股代码：", item['SECURITY_CODE_A'])
    print("A 股简称：", item['SECURITY_ABBR_A'])
    print("A 股总资本：", item['totalShares'])
    print("A 股流通资本：", item['totalFlowShares'])
    print("="*60)
'''

# level 2:
# 股市行情爬虫
# http://vip.stock.finance.sina.com.cn/mkt/#sh_a
# 爬取沪深两市A股，B股，AB股，深市债券，沪市债券信息，保存到myssql数据库

'''

import requests
import json
import pymysql
import re
import math


con = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='python_spider')
cur = con.cursor()
count_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeStockCount?'
data_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?'
type_list = ['sh_a', 'sh_b', 'sz_a', 'sz_b', 'sh_z', 'sz_z']
page = 1
size = 40
pat1 = re.compile(r'"(\d+)"')
pat2 = re.compile(r'\{(.*?)\}')
headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}

for type in type_list:
    params1 = {
        'node': type
    }
    html = requests.get(url=count_url, params=params1, headers=headers).text
    print(html)
    count = int(pat1.search(html).group(1))
    page_count = math.ceil(count / size)
    # print(count, page_count)
    for page in range(1, page_count + 1):
        params2 = {
            'page': page,
            'num': 40,
            'sort': 'symbol',
            'asc': '1',
            'node': type,
            '_s_r_a': ' init'
        }
        print('='*50, type, 'page:', page, '='*50)
        html = requests.get(data_url, params=params2, headers=headers).text
        #print(html)
        ls = pat2.findall(html)
        for item in ls:
            print(item)
            tmps = item.split(',')
            for temp in tmps:
                tmps2 = temp.split(':')
                print(tmps2[0],'=====',tmps2[1])
                # sql = 'insert into 股市行情(id, %s)values(%s, %s)'
                # cur.execute(sql, (temp[0], 0, temp[1]))
                # print('存储中...')
'''

# 海报图片爬虫
# http://www.haibao.com/
# http://pic.haibao.com/piclists/
# 爬取海报图片
#





# 腾讯动漫爬虫
# https://new.qq.com/ch/comic/
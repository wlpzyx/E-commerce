import requests
from bs4 import BeautifulSoup

import json
import pymysql


def tencent(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

    respons =requests.get(url, headers)
    return respons.content


url = "https://www.quanben.net/4/4408/"
def texts():
    html = BeautifulSoup(tencent(url), 'lxml')
    results = html.select('dl.chapterlist > dd')
    # print(len(results))
    BAST_URL = 'https://www.quanben.net'
    print("小说名：", "《九星杀神》")
    for each in results:
        item = {}
        item['name'] = each.select_one('a').string
        item['url'] = BAST_URL + each.select_one('a')['href']

        html = tencent(url)
        html = BeautifulSoup(html, 'lxml')
        ls = html.select('dl.chapterlist > dd')
        # print(len(ls))
        for i in range(10):
            ls.pop(0)
        ier = BAST_URL + each.select_one('a')['href']
        html = tencent(ier)
        html = BeautifulSoup(html, 'lxml')
        item['content'] = html.select_one('#BookText').get_text()

        print("目录：", item['name'])
        print("链接：", item['url'])
        print('content:', item['content'])

        items = [item['name'], item['url'], item['content']]
        store(items)


def store(data):
    strSql = 'insert into jiuxingshashen VALUES(0,%s,%s,%s)'
    cur.execute(strSql, data)
    conn.commit()


if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='jiuxingshashen')
    cur = conn.cursor()
    texts()
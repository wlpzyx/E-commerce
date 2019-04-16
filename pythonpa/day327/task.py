from lxml import etree
import requests


def site():
    url = 'http://www.4399.com/?haoqqdh'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    # , headers=headers.decode(encoding='utf-8')
    request = requests.get(url,headers)
    return request.content.decode('gbk', 'ignore')


def allyouxi(html):
    html = etree.HTML(html)
    kk = html.xpath('//ul[@class="mi_ul"]/li')
    print("===================手游========================")
    for i in kk:
        content = i.xpath('./a//text()')[0]
        url = i.xpath("./a/@href")[0]
        print("名称：", content)
        print("URL:", url)
    liste = ['专辑', '动作', '益智', '体育', '女生']
    a = html.xpath('//a[@class="mi_tit"]')
    STANDBY_URL = 'http://www.4399.com'
    for i in a:
        bt = i.xpath("./text()")[0]
        if bt in liste:
            print("==================="+bt+"========================")

            li = i.xpath("./../div/span")
            for j in li:
                content = j.xpath("./a//text()")[0]
                print("名称：", content)
                url = j.xpath("./a/@href")[0]
                print("URL：", STANDBY_URL + url)

    print("===================网页游戏========================")
    sp = html.xpath('//div[@class="mi_web"]/span')
    print(len(sp))
    for s in sp:
        content = s.xpath('./a//text()')[0]
        url = s.xpath('./a/@href')[0]
        print("内容：", content)
        print("URL：", STANDBY_URL+url)


    print('=========================h5游戏==========================')
    span = html.xpath('//a[@class="h5_w"]/../div/span')
    print(len(span))
    for j in span:
        content = j.xpath('./a//text()')[0]
        print('内容：', content)
        url = j.xpath('./a/@href')[0]
        print('url：',  STANDBY_URL+url)
    print('===========================最新好玩小游戏列表======================')
    li = html.xpath('//div[@class="tm_fun h_3"]/ul/li')
    print(len(li))
    for i in li:
        content = i.xpath('./a//text()')[0]
        print('内容：', content)
        url = i.xpath('./a/@href')[0]
        print('url：', STANDBY_URL+url)
    # print('=============================4399精选游戏 h5游戏精选========================')
    div = html.xpath('//div[contains(@class,"h_4")]')
    for i in div:
        title = i.xpath('./div/a/text()')[0]
        print('=============================='+title+'==============================')
        li = i.xpath('./ul/li')
        print(len(li))
        for j in li:
            content = j.xpath('./a//text()')[0]
            print('内容：', content)
            url = j.xpath('./a/@href')[0]
            print('url：', STANDBY_URL + url)
    print('========================最新推荐游戏======================')
    ul = html.xpath('//div[@class="lf_game cf"]/ul')[0]
    li = ul.xpath('./li')
    print(len(li))
    for i in li:
        content = i.xpath('./a//text()')[0]
        print('内容：', content)
        url = i.xpath('./a/@href')[0]
        print('url：', STANDBY_URL + url)






if __name__ == "__main__":
    allyouxi(site())





















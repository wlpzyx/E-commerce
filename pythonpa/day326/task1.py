import requests
from lxml import etree



def req(params):
    URL = 'https://tieba.baidu.com/f'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    }
    response = requests.get(URL, headers=headers, params=params)
    # html = response.content.decode('utf8')
    html = response.content.decode()
    return html


def save(name, page, html):
    print(html)
    selector = etree.HTML(html)
    ls = selector.xpath('//li[contains(@class,"j_thread_list clearfix")]')
    print('len:', len(ls))
    result = etree.tostring(selector, pretty_print=True).decode()
    print(result)
    with open('./%s第%s页.html' % (name, page), 'w', encoding='utf8')as f:
        f.write(html)


if __name__ == '__main__':
    name = input('请输入贴吧名称》》》')
    start_page = int(input('请输入起始页》》》'))
    end_page = int(input('请输入结束页》》》'))
    kwange = {
        'kw':name,
        'ie':'utf-8',
        'pn':''
    }
    for i in range(start_page, end_page+1):
        if i <=1:
            kwange['pn'] = 1
            html = req(kwange)
            save(name, i, html)
        else:
            kwange['pn']=(i-1)*50
            html = req(kwange)
            save(name, i, html)
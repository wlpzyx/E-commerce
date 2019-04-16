import requests


datas = {}
datas['i'] = 'good'
datas['from'] = 'AUTO'
datas['to'] = 'AUTO'
datas['smartresult'] = 'dict'
datas['client'] = 'fanyideskweb'
datas['salt'] = '15535019561986'
datas['sign'] = 'd4dee838452698909eb7ea4d40dbd862'
datas['ts'] = '1553501956198'
datas['bv'] = '33a62fdcf6913d2da91495dad54778d1'
datas['doctype'] = 'json'
datas['version'] = '2.1'
datas['keyfrom'] = 'fanyi.web'
datas['action'] = 'FY_BY_REALTlME'
datas['typoResult'] = 'false'
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
Request_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
requests = requests.post(Request_URL, data=datas)


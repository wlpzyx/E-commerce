import requests


cs = {'wd': '长城'}
headers = {'User-Agent': 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
requests = requests.get('http://www.baidu.com/s?', params=cs, headers=headers)
print(requests.status_code)
print(requests.encoding)
print(requests.text)

import requests

url = 'http://www.4399.com/?haoqqdh'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

headers = requests.get(url, headers)
print(headers.text)

with open('xyx_4399.html', 'w', encoding='utf-8')as f:
    f.write(headers.text)




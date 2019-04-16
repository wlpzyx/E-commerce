import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

requests = requests.get('http://img.qqzhi.com/uploads/2018-12-14/110256340.jpg', headers=headers)
with open('./images/img.jpg', 'wb')as f:
    f.write(requests.content)



